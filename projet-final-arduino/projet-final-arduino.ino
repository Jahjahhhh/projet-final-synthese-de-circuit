#define LED0 10
#define LED1 11
#define LED2 12
#define LED3 13

void setup() {
  pinMode(LED0, OUTPUT);
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);

  Serial.begin(9600);
  while (!Serial)
    ;
}

byte data = 0;
void loop() {
  if (Serial.available() > 0) {
    data = Serial.read();
    Serial.write(data);
  }
  switch (data) {
    case 'A':
      digitalWrite(LED0, LOW);
      digitalWrite(LED1, HIGH);
      digitalWrite(LED2, HIGH);
      digitalWrite(LED3, HIGH);
      break;
    case 'B':
      digitalWrite(LED0, HIGH);
      digitalWrite(LED1, LOW);
      digitalWrite(LED2, HIGH);
      digitalWrite(LED3, HIGH);
      break;
    case 'C':
      digitalWrite(LED0, HIGH);
      digitalWrite(LED1, HIGH);
      digitalWrite(LED2, LOW);
      digitalWrite(LED3, HIGH);
      break;
    case 'D':
      digitalWrite(LED0, HIGH);
      digitalWrite(LED1, HIGH);
      digitalWrite(LED2, HIGH);
      digitalWrite(LED3, LOW);
      break;
  }
}