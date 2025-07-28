# Bonus Projemin Dokümantasyonu! 🚀

![Img](https://i.hizliresim.com/dm4cqa9.png)
Bu dokümantasyon, Flask kullanarak oluşturduğum bir web uygulamasının nasıl çalıştırılacağı ve projenizin temel işlevleri hakkında bilgi içermektedir. Kendi deneyimimden yola çıkarak size adım adım rehberlik edeceğim. Ayrıca, projenin canlı çalışan versiyonunu [stayhard.com.tr](http://stayhard.com.tr) adresinde görebilirsiniz.

## 🎯 Proje Amacı

Bu proje, kullanıcıların çevrimiçi kitapları satın almasını veya okumasını sağlayan basit bir web uygulamasını hedeflemektedir. Kullanıcılar, bir e-posta adresi aracılığıyla giriş yapar, kitapları görüntüler ve satın alır veya okur. Projeyi nasıl çalıştırabileceğinizi ve özelleştirebileceğinizi aşağıda adım adım açıklayacağım. Projedeki temel özellikler ise şunlardır:

- Kullanıcı Girişi
- E-posta Doğrulama
- Kitapları Görüntüleme
- Kitap Satın Alma veya Okuma
- Tema ve Stil Seçenekleri

## 🚀 Nasıl Çalıştırılır?

Projenizi çalıştırmak ve internet üzerinde yayınlamak için aşağıdaki adımları izleyebilirsiniz:

### Adım 1️⃣: Amazon EC2 Üzerinde Sanal Makine Oluşturma

Amazon Web Services (AWS) üzerinde bir Windows sanal makine (Instance) oluşturun. Bu sanal makine, projenizi barındırmak için kullanılacaktır.

### Adım 2️⃣: Sanal Makineye Bağlanma

Sanal makineye erişmek için RDP (Remote Desktop Protocol) istemcisi kullanın. Ayrıca, .PEM dosyasındaki şifreyi çözerek erişiminizi sağlayın.

### Adım 3️⃣: Proje Dosyalarını Yükleme

Projeyi yerel bilgisayarınızdan sanal makinenize kopyalayın. Bu adım, projenizin kaynak kodlarını içeren dosyaların sanal makinenize taşınmasını sağlar.

### Adım 4️⃣: Python Kurulumu

Sanal makinenizde Python'un en son sürümünü kurun. Bu adım, Flask uygulamanızın çalışması için gereklidir.

### Adım 5️⃣: Proje Dizinine Gitme

Sanal makinenizde komut istemcisini açın ve projenizin bulunduğu dizine gidin. Örneğin:

```
cd ProjeYolu
```

### Adım 6️⃣: Uygulamayı Çalıştırma

Flask uygulamanızı başlatmak için aşağıdaki komutu kullanın:

```
python main.py
```

Bu komut, projenizi yerel sunucunuzda çalıştıracak ve belirli bir IP adresi ve bağlantı noktası üzerinden erişilebilir hale getirecektir.

### Adım 7️⃣: Hosting Hizmeti Sağlama

Sanal makinenizde çalışan Flask uygulamanızı internete açmak için sanal makinenizin IP adresini kullanın. Bu, projenizin geçici bir URL'si olacaktır. Örneğin, `http://51.20.1.29/` gibi bir IP adresi olabilir.

### Adım 8️⃣: Özel Domain Kullanma

Daha profesyonel bir görünüm elde etmek için hosting.com.tr veya benzer bir domain sağlayıcısından bir domain satın alın. Ardından, bu domaini sanal makinenizin IP adresi ile yönlendirerek projenizi özel bir domain üzerinde çalıştırabilirsiniz.

### Adım 9️⃣: Özelleştirmeler

Projeyi kişiselleştirmek için aşağıdaki adımları izleyin:

#### 1. Shopier API Anahtarları

- `main.py` dosyasında bulunan `"Bearer API_KEY"` ifadesini, kendi Shopier API

 anahtarınızla değiştirin.

#### 2. SMTP Ayarları

- `"YOUR_GMAIL"` ve `"YOUR_PASSWORD_OF_GMAIL"` ifadelerini, kendi Gmail adresiniz ve şifrenizle değiştirin. Bu, e-posta doğrulama işlemleri için kullanılır.

#### 3. Ürün ID'leri

- `get_emails` fonksiyonunda, `"YOUR_PRODUCT_ID"` ifadesini, Shopier hesabınızda oluşturduğunuz ürün ID'leri ile değiştirin.

### Adım 🔟: Projeyi Canlıya Alma

Projeniz artık canlı! Tarayıcınızda projenizin URL'sini ziyaret ederek kullanabilirsiniz. Örneğin, [stayhard.com.tr](http://stayhard.com.tr).

## 🔍 Kodların Ana İşlevleri

Proje içindeki Python kodlarının ana işlevleri şunlardır:

### `main.py` İşlevleri

1. **Kullanıcı Girişi ve Oturum Yönetimi**

   - `User` sınıfı, kullanıcıları temsil etmek için kullanılır.
   - `load_user` fonksiyonu, kullanıcıları ID'leriyle yüklemek için kullanılır.
   - `login_manager` ile oturum yönetimi sağlanır.

2. **E-posta Adreslerini API'den Getirme**

   - `get_emails` fonksiyonu, API'den müşteri e-posta adreslerini çeker ve `customer_emails` listesine depolar.

3. **Ana Sayfa (`/`)**

   - `main` fonksiyonu, ana sayfayı temsil eder ve `main.html` şablonunu döndürür.

4. **E-posta Doğrulama İşlemi**

   - `create_verification_code` fonksiyonu, rastgele bir doğrulama kodu oluşturur.
   - `send_code_to_mail` fonksiyonu, kullanıcıya e-posta ile doğrulama kodu gönderir.

5. **Kitapları Görüntüleme ve Yönlendirme**

   - `login` fonksiyonu, kullanıcının kitapları görüntülemesi için giriş yapmasını sağlar.
   - `check_verification` fonksiyonu, kullanıcının doğrulama kodunu kontrol eder ve kitapları yönlendirir.

6. **Kitap Sayfaları**

   - `firstbook` ve `secondbook` fonksiyonları, kullanıcının kitapları görüntülemesini sağlar.

### HTML Dosyaları İşlevleri

1. **`main.html`**: Ana sayfa tasarımını içerir. Kullanıcının kitapları görüntüleyebilmesi için bir kart tasarımı sunar.

2. **`login.html`**: Kullanıcının e-posta adresini girebileceği bir form sunar.

3. **`verification.html`**: Doğrulama kodunu girmek için bir form sunar.

4. **`firstbook.html` ve `secondbook.html`**: Kitap sayfalarının tasarımını içerir. Kullanıcıların kitapları okuyabilmesi için bir görünüm sunar.

5. **`error_page.html`**: Hataları ve uyarıları gösteren bir sayfa tasarımı sunar.

## 🧰 Teknolojiler ve Kütüphaneler

- **Flask**: Web uygulaması geliştirmek için kullanılan Python çerçevesi.
- **Flask-Login**: Kullanıcı oturumu yönetimi için kullanılan Flask eklentisi.
- **requests**: API çağrıları yapmak için kullanılan Python modülü.
- **smtplib ve email**: E-posta doğrulama işlemleri için kullanılan Python modülleri.
- **HTML ve CSS**: Kullanıcı arayüzünü oluşturmak için kullanılan temel web teknolojileri.

## 📁 Dosya Dizini

Proje dosya dizini aşağıdaki şekildedir:

```
- Bonus Project
    - static
        favicon.ico
        main.css
        pdf.css
        style.css
        pdf.js
        pdf.worker.js
    - templates
        error_page.html
        firstbook.html
        login.html
        main.html
        secondbook.html
        verification.html
    main.py
    README.md
```

## 📂 Dosya Açıklamaları

- `main.py`: Flask uygulamasının ana dosyasıdır. Kullanıcı girişi, e-posta doğrulama, kitap görüntüleme ve yönlendirme işlemlerini içerir.

- `static`: Stil dosyaları ve favicon gibi statik dosyaların bulunduğu klasördür.

- `templates`: Flask uygulamanızın HTML şablonlarını içeren klasördür.

## 🧑‍💻 Python Kodlarının İşlevleri

Proje içindeki Python kodları aşağıdaki işlevlere sahiptir:

- Kullanıcı girişi ve oturum yönetimi.
- E-posta doğrulama ve e-posta gönderme işlemleri.
- API kullanarak kitapları görüntüleme.
- Kullanıcının kitapları satın alma veya okuma işlemleri.

## 🌐 HTML Dosyaları

Projedeki HTML dosyaları, kullanıcı arayüzünün tasarlandığı ve Flask ile birleştirildiği dosyalardır. HTML dosyaları, kullanıcıların kitapları görüntülemesini ve işlemlerini gerçekleştirmesini sağlar.

---
