#define LEDPIN 11

void setup(){
    Serial.begin(9600);
    pinMode(LEDPIN, OUTPUT);
}
 
void loop(){
    if (Serial.available()) {
        byte nr = Serial.read();
        Serial.print("Folgender char wurde empfangen: ");
        Serial.println(nr, DEC);
        analogWrite(LEDPIN, 80);
        delay(500);
        analogWrite(LEDPIN,0);
        delay(500);
    }
}
