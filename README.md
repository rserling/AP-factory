# Ambiguous Productions
This project will automate the processing and release of video files, resulting in a media production pipeline. It is ambitious, adds questionable value and probably a spectacular _Frittering and Wasting of Hours_. But good excersize? 

## Components

### KB Studio
Video files are generated from end of manual design process in Karaoke Builder Studio  on Windows (only).
### Task Scheduler: Batch
Raw AVI is output manually to a watched folder in Windows. A batch script finds new files and copies them to the processing host (MacOS).
### Cron Entry: Python
A **python** script does the following: 
* validates new **AVI** files
* transcodes them to **MP4**, validates the result
* copies the successful result to a shared Google Drive folder
* logs all activities
* creates a release notification for consumers

## Dependencies
* python 3
* SSH authentication with unattended key exchange
* windows batch file on 
* ffmpeg
* MacOS Cron
* Windows Task Scheduler
