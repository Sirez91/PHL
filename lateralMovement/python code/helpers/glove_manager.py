def vibrateFor(song):
    vibration_message = getVibrationMessage(song);
    
    i = 0
    leds = [];
    while i < len(song):
        ledsAtTheSameTime = [];
        ledsAtTheSameTime.append(str(notes_to_led.get(song[i][0])));
        if i+1 != len(song) and song[i+1][2] == 0:
            ledsAtTheSameTime.append(str(notes_to_led.get(song[i+1][0])));
            i = i+2
        else:
            i = i+1
        leds.append(';'.join(ledsAtTheSameTime));
    return ','.join(leds);