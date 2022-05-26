# Ian Royer
# Stopwatch Runner and UI

import stopwatch
import PySimpleGUI as sg

defaultmessage = "0m 0.0s"

# The layout for the window being created
win_layout = [
        [sg.Text("Stopwatch",size=(200, 1), justification="center")],
        [
            sg.Text(defaultmessage, size = (200, 1), justification="center", key="-TIMETEXT-")
        ],
        [sg.HorizontalSeparator()],
        [
            sg.Button("Start", key="-START-", size = (6, 1)),
            sg.Button("Stop", key="-STOP-", size = (6, 1)),
            sg.Button("Reset", key="-RESET-")
        ]
    ]

watch = stopwatch.StopWatch()
window = sg.Window("Simple Stopwatch", win_layout, size=(200,100))

#Event Loop
while True:

    # if(watch.isRunning()):
    #     window["-TIMETEXT-"].update("%.2fs" % watch.get_diff())
    #     print("ping")
    #     window.refresh()

    event, values = window.read() 

    if event == "-START-":
        watch.start()
        window["-TIMETEXT-"].update("Running...")
        window["-START-"].update(disabled = True)
    
    if event == "-STOP-":
        dif = watch.get_diff()
        window["-TIMETEXT-"].update("%dm %.2fs" % (dif/60, dif%60))
        watch.stop()
        window["-START-"].update(disabled = False)

    if event == "-RESET-":
        watch.reset()
        window["-TIMETEXT-"].update(defaultmessage)
        window["-START-"].update(disabled = False)
    
    if event == sg.WIN_CLOSED:
        break

#Close when done
window.close()
