---
date: 2022-11-28
author: Tim Hunter (thunte27@uwo.ca)
---
# Medical records app

## Input

medical entries. Entries may be doctor appointments, picking up meds, changing meds, any time you get sick, or tracking any of your medical or fitness data.
medical records include [date, description, attachments, doctors/institutions, medications, {personal health data}]

## Features

### Modern UI with customtkinter

GUI is modern and user friendly. Implemented using the customtkinter library, this app offers a sleek user experience.

### Medical record form

Enter individual medical records using the text form.

### View a list of your medical records

View all your past medical records in a table form. This view includes a pagination feature, with the possibility to extend variable page lengths.

### Perpetual data storage

This app keeps your data stored on the disk so you don't have to worry about losing the data when you close the app.

## Roadmap

- improve entry form and data structure
- login with password
- encrypting data
- add file attachments
- improve ui with toolbar and more uniform views
- entry display views:
  - list view
  - filtering
  - gantt view for medications/other
  - maybe charts
- save records as a text file and encrypted
