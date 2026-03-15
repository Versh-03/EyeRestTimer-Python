# EYE REST TIMER 

The 20-20 Eye Rest Timer is a simple Python desktop application built using Tkinter that helps reduce eye strain during long screen sessions. The program reminds users to follow the 20-20 rule — every 20 minutes, look away for 20 seconds.
When the timer completes, the application displays a fullscreen translucent overlay to prompt the user to take a short eye break.
The project demonstrates the use of Python's Tkinter library for GUI creation, timers, and basic screen management.


## The Logic and Design

The program functions as a background loop that alternates between a "Work" state and a "Break" state.
Work State: For 20 minutes, the application is completely withdrawn from the UI, sitting idle in the background to save system resources.
Break State: Every 20 minutes, a full-screen overlay appears for 20 seconds.

Visuals: It uses Gainsboro ("#DCDCDC") at 100% opacity as pure white is too straining.


## Technology and Implementation
The script is built entirely on the Python standard library using Tkinter.

- Timing: Instead of using resource-heavy threading, it utilizes the root.after() event loop. This allows the computer to "sleep" between state changes without hanging the application.

- Input Management: To make the break effective, the script uses root.focus_force() and root.grab_set(). These commands ensure the overlay stays on top and "swallows" mouse and keyboard events, preventing clicking back into other applications during the break..

- Safety: It uses the Escape key to root.destroy(), providing an immediate kill-switch for the process in case of emergencies such as Meetings.
