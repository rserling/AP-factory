import os
import subprocess
import datetime
from pathlib import Path
import shutil
import sys
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='C:/Users/LENOVO/logz/process-avi.log', filemode='a'
)
logger = logging.getLogger(__name__)

def process_new_files(directory, flag_file, command, parameter, source_ext, target_ext):
    """
    Process files newer than the flag file with a fixed parameter and target extension.
    
    Args:
        directory (str): Directory to monitor
        flag_file (str): Path to the completion flag file
        command (str): Command to run
        parameter (str): Fixed parameter to pass to command
        source_ext (str): Source file extension to look for
        target_ext (str): Target file extension for output
    """
    try:
        # Ensure extensions start with dot
        source_ext = f".{source_ext.lstrip('.')}"
        target_ext = f".{target_ext.lstrip('.')}"

        # Get flag file modification time
        flag_path = Path(flag_file)
        logger.info(f"Checking mod time of file {flag_path}")
        if not flag_path.exists():
            flag_path.touch()
            logger.info(f"Created new flag file: {flag_path}")
        
        flag_time = flag_path.stat().st_mtime
        if not flag_time:
            logger.info(f"timestamp of {flag_file} not obtained, flag_time has no value")
        else:
            logger.info(f"timestamp of {flag_file} is {flag_time}")

        # Find files newer than flag file with specified extension
        directory_path = Path(directory)
        new_files = [
            f for f in directory_path.glob(f'*{source_ext}')
            if f.is_file() 
            #and f.stat().st_mtime > flag_time 
            and f != flag_path
        ]

        if not new_files:
            logger.info(f"No new files with extension {source_ext} to process at {directory_path}")
            return

        end_dir = "G:/My Drive/kbuild/Ambiguous Productions"
        final_path = Path(end_dir)

        # Process each new file
        for source_path in new_files:
            try:
                # Create target filename with new extension
                target_path = source_path.with_suffix(target_ext)
                # Construct command with parameter and target filename
                cmd_parts = [
                    'ffmpeg', '-y', '-i', source_path.name, '-pix_fmt', 'yuv420p', target_path.name
                ]
                
                # Run the command
                logger.info(f"Processing: {source_path}")
                logger.info(f"Tryna run: {cmd_parts}")
                os.chdir(directory_path)
                result = subprocess.run(
                    cmd_parts,
                    capture_output=True,
                    shell=False,
                    text=True
                )

                # Check if command was successful
                if result.returncode == 0:
                    # Append to flag file with just the filename and timestamp
                    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    with open(flag_file, 'a') as f:
                        f.write(f"{timestamp} - {target_path.name}\n")
                    
                    # Delete source file
                    source_path.unlink()
                    logger.info(f"Processed and deleted: {source_path.name}")

                    # Copy file to Drive
                    try:
                      shutil.copy(target_path.name, final_path)
                    except EnvironmentError:
                       logger.error(f"Unable to copy file {target_path.name} to {final_path}")
                    else:
                       logger.info(f"Copied to GDrive: {target_path.name}")
                else:
                    logger.error(f"Command failed for {source_path.name}: {result.stderr}")


            except Exception as e:
                logger.error(f"Error processing {source_path}: {str(e)}")

    except Exception as e:
        logger.error(f"Error in process_new_files: {str(e)}")

def main():
    directory = "C:/Users/LENOVO/kbuilds"
    flag_file = "C:/Users/LENOVO/kbuilds/processed.txt"

    command = "ffmpeg -n -i"
    parameter = "-pix_fmt yuv420p"
    source_ext = "avi" 
    target_ext = "mp4" 

    process_new_files(directory, flag_file, command, parameter, source_ext, target_ext)

if __name__ == "__main__":
    main()

