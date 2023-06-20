<h1 align="center">🤖 English in 16 hours Bot</h1>

#### Let's learn English in 16 hours using the method of Dmitry Petrov.

Bot example [@nPolyglot16enBot](https://t.me/nPolyglot16enBot)

## Requirements

* Python 3.10 and above.
* Docker and docker-compose.

## Usage

Go to the project folder

```bash
cd polyglot16en-bot
```

Create environment variables file

```bash
cp .env.example .env
```

Edit [environment variables](#environment-variables-reference) in `.env`

```bash
nano .env
```

### Launch using Docker

1. Install [docker](https://docs.docker.com/get-docker) and [docker compose](https://docs.docker.com/compose/install/)

2. Build and run your container
   ```bash
   docker-compose up -d
   ```

### Environment variables reference

| Variable   | Type | Description                                             |
|------------|------|---------------------------------------------------------|
| REDIS_HOST | str  | Set "redis" if you will be using docker                 |
| BOT_TOKEN  | str  | Token, get it from [@BotFather](https://t.me/BotFather) |
| DEV_ID     | int  | Developer's Telegram ID                                 |
| DB_USER    | str  |                                                         |
| DB_PASS    | str  |                                                         |
| DB_HOST    | str  |                                                         |
| DB_PORT    | int  |                                                         |
| DB_NAME    | str  |                                                         |
