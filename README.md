# Dalonline Find Time Utility

A helper schedule app for Dalhousie University's academic timetable.

## Usage
```bash
python3 extract_data.py <html file> # Extract info from html output to a file called results
python3 display.py <results file> # Displays a list of classes with names.
python3 display.py <results file> [classes...] # Displays the timetable featuring those classes
```

## Disclaimer
I do not own the dal online system, nor do I want this to be thought of as official in any way.
This tool is just to help visualise classes in a better way.

## TODO
  * [ ] Make it more visualy, perhapse replace terminal graphics with html and js
  * [ ] Add a script to download all pages of a section
  * [ ] Make it work for sections that are not CSCI
  * [ ] Consider how to improve visuals...
  * [ ] More colors, more options with that...
  * [ ] Help menu.
  * [ ] Wraper script do preform downloads, processing, and display all in one.
  * [ ] Consider what widths actualy mean, could we use them to mean something like level?
  * [ ] In legend put widths.
