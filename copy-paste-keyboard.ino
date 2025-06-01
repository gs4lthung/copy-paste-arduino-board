#define COPY_BUTTON 3
#define PASTE_BUTTON 2
#define LED_1 13
#define LED_2 12

void setup() {
  Serial.begin(9600);
  pinMode(COPY_BUTTON, INPUT_PULLUP);
  pinMode(PASTE_BUTTON, INPUT_PULLUP);
  pinMode(LED_1, OUTPUT);
  pinMode(LED_2, OUTPUT);
}

void loop() {
  if (digitalRead(COPY_BUTTON) == 0) {
    Serial.println("COPY");
    digitalWrite(LED_1, HIGH);
    delay(200);
    digitalWrite(LED_1, LOW);

  }

  if (digitalRead(PASTE_BUTTON) == 0) {
    Serial.println("PASTE");
    digitalWrite(LED_2, HIGH);
    delay(200);
    digitalWrite(LED_2, LOW);

  }
}
