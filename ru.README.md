# bitsender
Скрипт для отправки биткоинов на несколько кошельков одной транзакцией.

## Установка
### Клонировать репозиторий
```shell
git clone https://github.com/exelay/bitsender.git
cd bitsender
```
### Создать виртуальное окружение
```shell
python3 -m venv venv
source venv/bin/activate
```
### Установить зависимости 
```shell
pip install -r requirements.txt
```
### Создать файл конфигурации
```shell
cp configurations/example.config.yaml configurations/config.yaml
```
## Использование
### Обновить файл конфигурации
Открыть `config.yaml` файл любым текстовым редактором 
и заполнить все поля своими данными. Сохранить изменения.

Например:
```shell
vim config.yaml
```
```yaml
# Список получателей.
# В квадратных скобках: адрес биткоин кошелька, сумма денег и валюта. (usd или btc)
# Все деньги отправляются в btc, если вы указали, к примеру, 10 usd,
# то они будут автоматически конвертированы в btc, согласно текущему курсу.
recipients:
  - [mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB, 10, usd]
  - [tb1ql7w62elx9ucw4pj5lgw4l028hmuw80sndtntxt, 0.0015, btc]

# Комиссия за один байт.
# Можете оставить это поле пустым, тогда комиссия будет рассчитана автоматически,
# исходя из общесреднего значения.
fee: 70

# Приватный ключ кошелька, с которого будет произведён расчёт.
key: cPmJ6LdYHeX46pJGvi5hbbmHjDGQQ1goCbBZEyNk5b2UG7GX6FkS
```

### Запустить скрипт
```shell
python bitsender.py run
```
С таким запуском, скрипт по умолчанию возьмёт все данные из файла `config.yaml`.
### Поддержка разных конфигураций
Если вы хотите создать разные файлы конфигураций, 
хранить их отдельно и запускать в зависимости от ситуации, вы можете это сделать. 
Просто создать копию файла `config.yaml` и переименовать его.

Например:
```shell
cp config.yaml custom-config.yaml
```
Затем запустить скрипт командой:
```shell
python bitsender.py run path/to/the/custom-config.yaml
```
Где `path/to/the/custom-config.yaml` это путь к нужному файлу конфигурации.
