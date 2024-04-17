
float Time0;
float Time1;
float Time2;
bool R_LED_ON = false;
bool L_LED_ON = false;
bool Start =false;
bool END =false;
bool ERR=false;

int count = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(9,OUTPUT); //右
  pinMode(6,OUTPUT); //左
  pinMode(14,INPUT); //右のセンサ用
  pinMode(15,INPUT); //左のセンサ用
  pinMode(4,OUTPUT); //ビープ用
  Time0=0;
  Time1=0;
  Time2=0;
  
}

void loop() {
  
  // put your main code here, to run repeatedly:
  if(digitalRead(10)==1 &&R_LED_ON==false && L_LED_ON==false){
    randomSeed(analogRead(0)); //これで完全ランダム値が作れる
    int off_time =random(500,5000);
    int choice = random(0,1000);
    //Serial.println(choice);
    delay(off_time);

    if(choice%2==0){
      R_LED_ON=true;
    }else{
      L_LED_ON=true;
    }

    Time0=micros();
    Start =true;
    
  }else{
    //入力がoffのとき
    //LED_ON = false;
    
  }

  if(Start&&digitalRead(10)==0){
    //LED点灯して手を離した時
    Time1=micros();
    Start=false;
  }

  if(R_LED_ON){
    
    if(digitalRead(14)==1){
      //右のセンサが反応
      Time2=micros();
      R_LED_ON=false;
      END =true;
      Correct();
      count ++;
    }else if(digitalRead(15)==1){
      //左のセンサが反応 つまり間違い
      ERR =true;
      Tone(200);
    }
    digitalWrite(9,HIGH);
    
  }else{
    digitalWrite(9,LOW);
  }

  if(L_LED_ON){
    
    if(digitalRead(15)==1){
      //左のセンサが反応
      Time2=micros();
      L_LED_ON=false;
      END =true;
      Correct();
      count ++;
    }else if(digitalRead(14)==1){
      //右のセンサが反応　つまり間違い
      ERR =true;
      Tone(200);
    }
    digitalWrite(6,HIGH);
  }else{
    digitalWrite(6,LOW);
  }


  if(END){
    String delta_Time1 =String(Time1 -Time0);
    String delta_Time2 =String(Time2 -Time1);
    String msg = "{ \"Time1\":" 
                    + delta_Time1
                    + ",\"Time2\":" 
                    + delta_Time2
                    + "}";
      Serial.println(msg);
    END =false;
  }

  if(ERR){
    R_LED_ON = false;
    L_LED_ON = false;
    ERR = false;
    Serial.println("ERR");
  }

 
  


  
}

void Tone(int f){

  tone(5,f,500);
  //delay(200);
  //noTone(5);
  
  
  }


void Correct(){
  tone(5,800,100);
  delay(100);
  tone(5,400,100);
  delay(100);
}
