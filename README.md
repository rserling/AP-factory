# Ambiguous Productions
This project automates the processing and release of video files, resulting in a sort of media production pipeline. It is ambitious, adds questionable value and probably a spectacular _Frittering and Wasting of Hours_. But good excersize? 

## Background
Due to compute resource limitations, transcoding and validation should happen directly on the client (design/production) machine, before the result is published to cloud resources (Google Drive) 

## Components

### KB Studio
Video files are generated from end of manual design process in Karaoke Builder Studio  on Windows (only).

### Task Scheduler: Python 
Raw AVI is output manually to a watched folder in Windows. 

A python script finds new **avi** files, transcodes them to **mp4** and copies them to the shared Google Drive path.
* Script: **process-avi.py**
* Task Scheduler Entry: **Process AVI Files**, daily at various times
* logs all activities _(logging still needs work)_
* creates a release notification for consumers _(still WIP)_

## Dependencies
* python 3
* ffmpeg
* python script on KB Studio "appliance" (Lenovo)
* dedicated mount to Google Drive (via GD Desktop App)
* Windows Task Scheduler
