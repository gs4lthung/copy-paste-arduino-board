#include <LiquidCrystal_I2C.h>
#define COPY_BUTTON 3
#define PASTE_BUTTON 2
#define LED_1 13
#define LED_2 12
#define COPY_STR "Ctrl + C"
#define PASTE_STR "Ctrl + V"

LiquidCrystal_I2C lcd(0x27, 20, 4);

void setup() {
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("Arduino Trigger");
  lcd.setCursor(0, 1);
  lcd.print("Copy & Paste");

  Serial.begin(9600);
  pinMode(COPY_BUTTON, INPUT_PULLUP);
  pinMode(PASTE_BUTTON, INPUT_PULLUP);
  pinMode(LED_1, OUTPUT);
  pinMode(LED_2, OUTPUT);
}



void loop() {
  trigger(COPY_BUTTON, COPY_STR, LED_1);
  trigger(PASTE_BUTTON, PASTE_STR, LED_2);
}

 void trigger(int button, String msg, int led) {
  if (digitalRead(button) == 0) {
    Serial.println(msg);
    lcd.clear();
    lcd.print(msg);
    digitalWrite(led, HIGH);
    delay(200);
    digitalWrite(led, LOW);
  }
}
