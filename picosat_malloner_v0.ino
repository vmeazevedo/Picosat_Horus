/* 
Autor: Vinícius Azevedo
Github: https://github.com/vmeazevedo
LinkedIn: https://www.linkedin.com/in/vin%C3%ADcius-azevedo-45180ab2/

Você pode encontrar o projeto completo no diretório abaixo:
https://github.com/vmeazevedo/Picosat_Malloner
*/


// Incluir Bibliotecas
#include "Arduino.h"
#include "DHT.h"
#include "SFE_BMP180.h"
#include "Wire.h"
#include "RTClib.h"
#include "SD.h"

// Definições de Pin
#define AM2302_PIN_SIG	2
#define SDFILE_PIN_CS	10

// inicialização de objeto
DHT am2302(AM2302_PIN_SIG);
SFE_BMP180 bmp180;
RTC_DS3231 rtcDS;
File sdFile;

void setup() 
{
    Serial.begin(9600);
    while (!Serial) ; // aguarde a conexão da porta serial. Necessário para USB nativo
    Serial.println("Inicializando");
    
    am2302.begin();
	
    //Inicializar dispositivo I2C
    bmp180.begin();
    
	if (! rtcDS.begin()) {
    Serial.println("Não foi possível encontrar RTC");
    while (1);
    }
    
	if (rtcDS.lostPower()) {
    Serial.println("RTC perdeu a bateria, vamos definir a hora!");
    // a linha seguinte define o RTC para a data e hora em que este esboço foi compilado
    rtcDS.adjust(DateTime(F(__DATE__), F(__TIME__)));
    // Esta linha define o RTC com uma data e hora explícitas, por exemplo, para definir
    // 21 de janeiro de 2014 às 3h:
    // rtcDS.adjust(DateTime(2014, 1, 21, 3, 0, 0));
    }
	
    // Defina o pino SPI SS para saída, caso contrário, as funções da biblioteca SD não funcionarão.
    // O SD é configurado para usar SPI SS Arduino pino 10 como seleção de chip (CS) por padrão.
    // Para alterar o pin, use SD.begin (SD_CS_PIN)
    pinMode(SDFILE_PIN_CS, OUTPUT);
    // Verifique se o cartão está presente e pode ser inicializado
    
	if (!SD.begin()) {
    Serial.println(F("O cartão falhou ou não está presente"));
    while(1);
    }
    Serial.println(F("Cartão inicializado"));
}


void loop() 
{
    // Sensor de umidade e temperatura AM2302
    // Leitura de umidade em %
    float am2302Humidity = am2302.readHumidity();
    // Leitura da temperatura em Celsius, para Fahrenheit use .readTempF ()
    float am2302TempC = am2302.readTempC();
    Serial.print(F("Umidade: ")); Serial.print(am2302Humidity); Serial.print(F(" [%]\t"));
    Serial.print(F("Temp: ")); Serial.print(am2302TempC); Serial.println(F(" [C]"));

    // BMP180 - Sensor de pressão barométrica, temperatura, altitude
    // Leitura da altitude do sensor barométrico, observe que o sensor tem 1m de precisão
    double bmp180Alt = bmp180.altitude();
    double bmp180Pressure = bmp180.getPressure();
    double bmp180TempC = bmp180.getTemperatureC();     //See also bmp180.getTemperatureF() for Fahrenheit
    Serial.print(F("Altitude: ")); Serial.print(bmp180Alt,1); Serial.print(F(" [m]"));
    Serial.print(F("\Pressao: ")); Serial.print(bmp180Pressure,1); Serial.print(F(" [hPa]"));
    Serial.print(F("\Temp: ")); Serial.print(bmp180TempC,1); Serial.println(F(" [°C]"));

    // RTC - Relógio de tempo real
    // Isso exibirá a hora e a data do RTC. consulte RTC.h para obter mais funções, como rtcDS.hour(), rtcDS.month(), etc.
    DateTime now = rtcDS.now();
    Serial.print(now.month(), DEC);
    Serial.print('/');
    Serial.print(now.day(), DEC);
    Serial.print('/');
    Serial.print(now.year(), DEC);
    Serial.print("  ");
    Serial.print(now.hour(), DEC);
    Serial.print(':');
    Serial.print(now.minute(), DEC);
    Serial.print(':');
    Serial.print(now.second(), DEC);
    Serial.println();
    delay(1000);
    
	// Módulo Micro SD
    // O código de exemplo SD cria um arquivo datalog.txt para registrar os dados do sensor
    sdFile = SD.open("datalog.txt", FILE_WRITE);
    // se o arquivo existir no cartão SD, grave os dados do sensor
    if (sdFile) {
    // Gravar no arquivo os dados:
	// ddmmaaaa,hhmmss,umidade,temperatura,pressão,press_nível_do_mar,altitude
	
	// ddmmaaaa,hhmmss
	DateTime now = rtcDS.now();
	sdFile.print(now.day(), DEC);
    sdFile.print(now.month(), DEC);
    sdFile.print(now.year(), DEC);
    sdFile.print(",");
    sdFile.print(now.hour(), DEC);
    sdFile.print(now.minute(), DEC);
    sdFile.print(now.second(), DEC);
    
	// Umidade,Temperatura,Pressão,Pres_nível_do_mar,Altitude
	sdFile.print(","); 
	sdFile.print(am2302.readHumidity());
	sdFile.print(","); 
    sdFile.print(bmp.readTemperature());
    sdFile.print(",");    
    sdFile.print(bmp.readPressure());
    sdFile.print(",");
	sdFile.print(bmp.readSealevelPressure());	
	sdFile.print(",");  
    sdFile.print(bmp.readAltitude());
    
	// Fechar o arquivo
    sdFile.close();
    } 
    else {
    // Se o arquivo não abriu, imprime o erro
    Serial.println(F("Erro ao abrir o arquivo."));
  }
  delay(500);
}
    
