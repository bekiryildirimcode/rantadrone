# Docker ile kurulum

Proje klasöründe Docker ile başlatmak için aşağıdaki kodu çalıştırın:

    docker-compose up -d --build
Ardından tabloların veritabanına yüklenebilmesi için aşağıdaki kodu çalıştırın:

    docker-compose exec web python manage.py migrate

> Bu kod sayesinde tablolar veritabanında oluşturulacaktır. Bu kodu
> çalıştırmazsanız "SESSION" hatası alırsınız.

Superuser oluşturmak için aşağıdaki kodu çalıştırın:

    docker-compose exec web python manage.py createsuperuser
   

> Projeye öğe eklemek için superuser oluşturmalısınız.

 Şimdi http://127.0.0.1:8080/ adresine gidip projenin doğu çalışıp çalışmadığını kontrol edebilirsiniz.
 







# Accounts App
Üyelik oluşturma ve giriş yapma özellikleri bu app'ın altında bulunur.

# Drone App
Dronların sıralanması filterlenmesi ver kiralanması işlemler bu app'ın altında bulunur.

# Rented App
Rezervasyon yapılmış dronler ve geçmişte kiraladıkları dronlar bu app'ın altında bulunur. Datable ve Rest framework bu kısımda kullanılmıştır.
