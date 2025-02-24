@echo off
setlocal EnableDelayedExpansion

:: Configuration
set "FOLDER=C:\Users\LENOVO\kbuilds"
set "FILE_EXT=*.avi"
set "LOG_FILE=C:\Users\LENOVO\logz\process.log"
set "PROCESS_CMD=scp -i C:\Users\LENOVO\.ssh\len"
set "RESTOF_CMD=elyons@10.0.0.26:Music/kbuild/"

:: Create timestamp for log entries
for /f "tokens=2 delims==" %%I in ('wmic os get localdatetime /value') do set datetime=%%I
set "TIMESTAMP=%datetime:~0,4%-%datetime:~4,2%-%datetime:~6,2% %datetime:~8,2%:%datetime:~10,2%:%datetime:~12,2%"

:: Check if folder exists
if not exist "%FOLDER%" (
    echo %TIMESTAMP% ERROR: Folder %FOLDER% not found >> "%LOG_FILE%"
    exit /b 1
)

:: Process each file
for %%F in ("%FOLDER%\%FILE_EXT%") do (
    echo %TIMESTAMP% INFO: Processing file %%~nxF >> "%LOG_FILE%"
    
    :: Run the process command
    echo %TIMESTAMP% INFO: Running cmd %PROCESS_CMD% "%%F" %RESTOF_CMD% >> "%LOG_FILE%"
    call %PROCESS_CMD% "%%F" %RESTOF_CMD%
    
    :: Check if process was successful
    if !ERRORLEVEL! EQU 0 (
        echo %TIMESTAMP% SUCCESS: Processed %%~nxF >> "%LOG_FILE%"
        
        :: Delete the file
        del "%%F"
        if !ERRORLEVEL! EQU 0 (
            echo %TIMESTAMP% INFO: Deleted %%~nxF >> "%LOG_FILE%"
        ) else (
            echo %TIMESTAMP% ERROR: Failed to delete %%~nxF >> "%LOG_FILE%"
        )
    ) else (
        echo %TIMESTAMP% ERROR: Failed to process %%~nxF >> "%LOG_FILE%"
    )
)

echo %TIMESTAMP% INFO: Processing attempt over >> "%LOG_FILE%"
endlocal


:: open scp://elyons:@10.0.0.26/ -hostkey="ssh-ed25519 255 GrsKo64eJ5QXYFbyj1pg0jIqj7WH6AmL7WRmbLjM9q0" -privatekey="C:\Users\LENOVO\.ssh\len" -rawsettings AgentFwd=1

