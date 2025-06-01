#define COPY_BUTTON 3
#define PASTE_BUTTON 2

void setup() {
  Serial.begin(9600);
  pinMode(COPY_BUTTON, INPUT_PULLUP);
  pinMode(PASTE_BUTTON, INPUT_PULLUP);
}

void loop() {
  if (digitalRead(COPY_BUTTON) == 0) {
    Serial.println("COPY");
    delay(200);
  }

    if (digitalRead(PASTE_BUTTON) == 0) {
    Serial.println("PASTE");
    delay(200);
  }
}
