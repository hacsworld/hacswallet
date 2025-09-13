# HacsWallet — Own your keys, own your chain 🔑⛓️

HacsWallet — минималистичный open-source кошелёк и нода, которые можно запустить прямо у себя на компьютере.  
**Децентрализация начинается дома.**

---

## 🚀 Quick start

```bash
git clone https://github.com/hacsworld/hacswallet.git
cd hacswallet
docker compose up --build
```

---

## 🔥 Features
- Генерация и хранение приватных ключей локально
- Отправка/получение транзакций
- Лёгкая нода на FastAPI
- REST API для интеграции
- Docker + CI/CD поддержка

---

## 📡 API endpoints

- `GET /wallet/create` — создать новый кошелёк  
- `GET /wallet/balance/{address}` — проверить баланс  
- `POST /wallet/send` — отправить транзакцию  
- `GET /chain/height` — текущая высота цепочки  

---

## 🛠 Dev notes
- Всё хранится локально — никакого "чужого" сервера  
- Ключи — только у вас  
- Можно использовать как основу для своего блокчейна или кастомного DeFi-проекта  
