    #include <FastLED.h>
    #define LED_PIN     7
    #define NUM_LEDS    144
    CRGB leds[NUM_LEDS];
    String input;
    int led;
    int prevLed=0;
    int on;
    int ind;

    void playSong(String input) {
      leds[prevLed] = CRGB(0,0,0);
      ind = input.indexOf(',');  //finds location of first ,
      led = input.substring(0, ind).toInt();   //captures led data int
      prevLed = led;
      leds[led] = CRGB(5, 0, 0);
      FastLED.show();
      delay(1000);
      if (ind > 0) {
        playSong(input.substring(ind+1));
      } else {
        leds[led] = CRGB(0,0,0);
        FastLED.show();
      }
    }

    void songA() {
      Serial.write("songA");
//          1
//         [74,237,0],
//         2
//        [76,237,14],78
//        3
//        [77,237,14],80
//        4
//        [76,118,14],78
//        5
//        [74,118,7],
//        6
//        [76,237,7],78
//        7
//        [79,237,14],84
//        8
//        [72,237,14], 71
//        9
//        [76,237,14],78
//        10
//        [72,474,14] 71
        
//        note 1
           leds[74] = CRGB(5, 0, 0);
           FastLED.show();
           delay(434);
//        note 2
           leds[74] = CRGB(0, 0, 0);
           leds[78] = CRGB(5, 0, 0);
           FastLED.show();
           delay(434);
//        note 3
           leds[78] = CRGB(0, 0, 0);
           leds[80] = CRGB(5, 0, 0);
           FastLED.show();
           delay(434);
//        note 4
           leds[80] = CRGB(0, 0, 0);
           leds[78] = CRGB(5, 0, 0);
           FastLED.show();
           delay(216);
//        note 5
           leds[78] = CRGB(0, 0, 0);
           leds[74] = CRGB(5, 0, 0);
           FastLED.show();
           delay(216);
//        note 6
           leds[74] = CRGB(0, 0, 0);
           leds[78] = CRGB(5, 0, 0);
           FastLED.show();
           delay(434);
//        note 7
           leds[78] = CRGB(0, 0, 0);
           leds[84] = CRGB(5, 0, 0);
           FastLED.show();
           delay(434);
//        note 8
           leds[84] = CRGB(0, 0, 0);
           leds[71] = CRGB(5, 0, 0);
           FastLED.show();
           delay(434);
//        note 9
           leds[71] = CRGB(0, 0, 0);
           leds[78] = CRGB(5, 0, 0);
           FastLED.show();
           delay(434);
           //        note 10
           leds[78] = CRGB(0, 0, 0);
           leds[71] = CRGB(5, 0, 0);
           FastLED.show();
           delay(869);
//        reset
           leds[71] = CRGB(0, 0, 0);
           FastLED.show();
    }

void songB() {
      Serial.write("songB");
      //1
//        [72,434,0],
        //2
//        [74,434,25],
        //3
//        [76,434,25],
        //4
//        [72,434,25],
        //5
//        [79,869,25],
        //6
//        [77,434,48],
        //7
//        [74,434,483],
//        //8
//        [74,434,25],
        //9
//        [77,434,25],
//        //10
//        [76,434,25],
//        //11
//        [72,869,25]
        
//        note 1
           leds[71] = CRGB(5, 0, 0);
           FastLED.show();
           delay(434);
//        note 2
           leds[71] = CRGB(0, 0, 0);
           leds[74] = CRGB(5, 0, 0);
           FastLED.show();
           delay(434);
//        note 3
           leds[74] = CRGB(0, 0, 0);
           leds[78] = CRGB(5, 0, 0);
           FastLED.show();
           delay(434);
//        note 4
           leds[78] = CRGB(0, 0, 0);
           leds[71] = CRGB(5, 0, 0);
           FastLED.show();
           delay(434);
//        note 5
           leds[71] = CRGB(0, 0, 0);
           leds[84] = CRGB(5, 0, 0);
           FastLED.show();
           delay(434);
//        note 6
           leds[84] = CRGB(0, 0, 0);
           leds[80] = CRGB(5, 0, 0);
           FastLED.show();
           delay(434);
//        note 7
           leds[80] = CRGB(0, 0, 0);
           leds[74] = CRGB(5, 0, 0);
           FastLED.show();
           delay(434);
//        note 9
           leds[74] = CRGB(0, 0, 0);
           leds[80] = CRGB(5, 0, 0);
           FastLED.show();
           delay(434);
           //        note 10
           leds[80] = CRGB(0, 0, 0);
           leds[78] = CRGB(5, 0, 0);
           FastLED.show();
           delay(434);
           //        note 11
           leds[78] = CRGB(0, 0, 0);
           leds[71] = CRGB(5, 0, 0);
           FastLED.show();
           delay(869);
//        reset
           leds[71] = CRGB(0, 0, 0);
           FastLED.show();
    }

    void setup() {
      Serial.begin(9600);
      FastLED.addLeds<WS2812, LED_PIN, GRB>(leds, NUM_LEDS);
      
    }
    
    void loop() {

      if(Serial.available()){
        input = Serial.readStringUntil('\n');
        if( input == "reset"){
          for(int i = 0; i < NUM_LEDS; i++) {
            leds[i] = CRGB(0, 0, 0);
            FastLED.show();
          }
        } else if ( input == "songA") {
          songA();
        } else if (input == "songB") {
          songB();
        } else if (input.length() >= 5) {
          playSong(input);
        } else {
          led = input.toInt();
            if (prevLed == led) {
              leds[led] = CRGB(0,0,0);
              FastLED.show();
              delay(80);
            }
            leds[prevLed] = CRGB(0,0,0);
            prevLed = led;
            leds[led] = CRGB(5, 0, 0);
          FastLED.show();
        }
    }
    }
