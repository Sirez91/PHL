const int motorPin2 = 2;
const int motorPin3 = 3;
const int motorPin4 = 4;
const int motorPin5 = 5; //does not work, not enough power to spin the motor
const int motorPin7 = 7;
const int motorPin12 = 12;
String input_string;
int mltime = 350;
int mloffset = 100;

void setup()
{
  Serial.begin(9600);
  pinMode(motorPin2, OUTPUT);
  pinMode(motorPin3, OUTPUT);
  pinMode(motorPin4, OUTPUT);
  pinMode(motorPin5, OUTPUT);
  pinMode(motorPin7, OUTPUT);
  pinMode(motorPin12, OUTPUT);
  Serial.println("started");
}

void passiveSong(String keys){
  unsigned long start = millis ();
  unsigned long tim = 20000*60UL;
  while (millis () - start <= tim) {
//    Serial.println("calling method");
    playPassive(keys);
    delay(20000);
  }
}

void playPassive(String keys) { 
    int separator = keys.indexOf(',');
    String input = keys.substring(0, separator);
    int separatorDur = input.indexOf(':');
    int note = input.substring(0,separatorDur).toInt();
    mltime = input.substring(separatorDur+1).toInt();
    if (note == 2) {
        digitalWrite(motorPin2, HIGH);
        delay(mltime);
        digitalWrite(motorPin2, LOW);
        delay(mloffset);
      }
      if (note == 3) {
        digitalWrite(motorPin3, HIGH);
        delay(mltime);
        digitalWrite(motorPin3, LOW);
        delay(mloffset);
      }
      if (note == 4) {
        digitalWrite(motorPin4, HIGH);
        delay(mltime);
        digitalWrite(motorPin4, LOW);
        delay(mloffset);
      }
      if (note == 7) {
        digitalWrite(motorPin7, HIGH);
        delay(mltime);
        digitalWrite(motorPin7, LOW);
        delay(mloffset);
      }
      if (note == 12) {
        digitalWrite(motorPin12, HIGH);
        delay(mltime);
        digitalWrite(motorPin12, LOW);
        delay(mloffset);
      }
    if(keys.indexOf(",") > 0) {
      String rest = keys.substring(separator+1);
      if(rest.length() > 0) {
        playPassive(rest);
      }
    }
    
}

void playActive(int input) { 
    if (input == 2) {
        digitalWrite(motorPin3, LOW);
        digitalWrite(motorPin4, LOW);
        digitalWrite(motorPin7, LOW);
        digitalWrite(motorPin12, LOW);
        digitalWrite(motorPin2, HIGH);
      }
      if (input == 3) {
        digitalWrite(motorPin2, LOW);
        digitalWrite(motorPin4, LOW);
        digitalWrite(motorPin7, LOW);
        digitalWrite(motorPin12, LOW);
        digitalWrite(motorPin3, HIGH);
      }
      if (input == 4) {
        digitalWrite(motorPin2, LOW);
        digitalWrite(motorPin3, LOW);
        digitalWrite(motorPin7, LOW);
        digitalWrite(motorPin12, LOW);
        digitalWrite(motorPin4, HIGH);
      }
      if (input == 7) {
        digitalWrite(motorPin2, LOW);
        digitalWrite(motorPin3, LOW);
        digitalWrite(motorPin4, LOW);
        digitalWrite(motorPin12, LOW);
        digitalWrite(motorPin7, HIGH);
      }
      if (input == 12) {
        digitalWrite(motorPin2, LOW);
        digitalWrite(motorPin3, LOW);
        digitalWrite(motorPin4, LOW);
        digitalWrite(motorPin7, LOW);
        digitalWrite(motorPin12, HIGH);        
      } 
      if (input == 0) {
        digitalWrite(motorPin2, LOW);
        digitalWrite(motorPin3, LOW);
        digitalWrite(motorPin4, LOW);
        digitalWrite(motorPin7, LOW);
        digitalWrite(motorPin12, LOW);
      }
}

void loop()
{
  if (Serial.available() > 0) {
    input_string = Serial.readStringUntil('\n');
    int separator = input_string.indexOf(',');
    String mode = input_string.substring(0, separator);
    String rest = input_string.substring(separator+1);
    if(mode == "passive") {
//      Serial.println("is passive, sending: " + rest);
      passiveSong(rest);
    } else if (mode == "active") {
      Serial.println("entered active");
      playActive(rest.toInt());
    }
  }
//    if (Serial.available() > 0) {
//      input_string = Serial.readStringUntil('\n');
//      separator = input_string.indexOf(',');
//      input = input_string.substring(0, separator).toInt();
//      mltime = input_string.substring(separator+1).toInt();
//      if (input == 2) {
//        digitalWrite(motorPin2, HIGH);
//        delay(mltime);
//        digitalWrite(motorPin2, LOW);
//      }
//      if (input == 3) {
//        digitalWrite(motorPin3, HIGH);
//        delay(mltime);
//        digitalWrite(motorPin3, LOW);
//      }
//      if (input == 4) {
//        digitalWrite(motorPin4, HIGH);
//        delay(mltime);
//        digitalWrite(motorPin4, LOW);
//      }
//      if (input == 7) {
//        digitalWrite(motorPin7, HIGH);
//        delay(mltime);
//        digitalWrite(motorPin7, LOW);
//      }
//      if (input == 12) {
//        digitalWrite(motorPin12, HIGH);
//        delay(mltime);
//        digitalWrite(motorPin12, LOW);
//      }
//      if (input == 0) {
//        digitalWrite(motorPin2, LOW);
//        digitalWrite(motorPin3, LOW);
//        digitalWrite(motorPin4, LOW);
//        digitalWrite(motorPin7, LOW);
//        digitalWrite(motorPin12, LOW);
//      }
//      Serial.println("done");
//  }
}
