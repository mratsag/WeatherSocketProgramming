# WeatherSocketProgramming

Bu proje, C dili ile yazılmış bir istemci (client) ve Java ile yazılmış bir sunucu (server) uygulamasından oluşan, socket programlama temelli bir hava durumu sorgulama sistemidir. Kullanıcı, istemci tarafında şehir adını girerek hava durumu verisini sunucudan alır.

## 🛠 Proje Yapısı


```
WeatherSocketProgramming/
├── C_Client/             # C dili ile yazılmış client uygulaması
│   └── client.c
├── Java_Server/          # Java ile yazılmış server uygulaması
│   └── WeatherServer.java
└── README.md             # Proje açıklamalarını içeren dosya
```


## 💡 Amaç

Socket programlamayı pekiştirmek ve farklı diller arasında haberleşme (interoperability) sağlamak amacıyla geliştirilmiştir. Gerçek zamanlı veri alışverişi yapılmakta olup, kullanıcı tarafından girilen şehir ismine karşılık API üzerinden alınan hava durumu bilgileri döndürülmektedir.

## ⚙️ Kullanılan Teknolojiler

- Java (Server tarafı)
- C (Client tarafı)
- Socket Programming (TCP)
- Hava durumu API'si (örneğin: OpenWeatherMap – API anahtarı gerektirir)

## 🚀 Nasıl Çalıştırılır?

### 1. Sunucu (Java) Tarafı

1. Java ortamınızı kurun.
2. `WeatherServer.java` dosyasını derleyin ve çalıştırın:

```bash
javac WeatherServer.java
java WeatherServer
```

### 2. İstemci (C) Tarafı
gcc client.c -o client
./client


### 3. Kullanım
İstemci tarafında çalıştırıldıktan sonra şehir adı girilir.

Sunucu, hava durumu bilgilerini ilgili API'den alır ve istemciye gönderir.

İstemci, gelen veriyi ekranda görüntüler.

## ✍️ Geliştiren
Murat Sağ

mrat.sag@hotmail.com
