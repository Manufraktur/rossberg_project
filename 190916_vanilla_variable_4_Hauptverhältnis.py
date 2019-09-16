newPage(20,20)

# create small ui element for variables in the script
Variable([
    # create a variable called 'HV' for Hauptverhältnis
    # and the related ui is a Slider.
    dict(name="HV", ui="Slider",
            args=dict(
                # some vanilla specific
                # setting for a slider
                value=5,
                minValue=4,
                maxValue=6)),
    ], globals())

modul_width = HV
modul_height = 6
padding = 5
fill(1)
stroke(0.5)
strokeWidth(.05)
rect(padding, padding, modul_width, modul_height)

stroke(0)
strokeWidth(.2)
indicator_length = modul_height  / 20
line((padding, padding + (modul_height / 4)), (padding + modul_width, padding + (modul_height / 4)+3))

print("Hauptverhältnis, rounded: " + '{:.0f}'.format(HV) + ":6")
print("Hauptverhältnis, more precise: " + '{:.1f}'.format(HV) + ":6")
print("Actual width of rect: " + str(HV))