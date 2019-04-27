# Linky to InfluxDB

**Linky to InfluxDB** is a Docker image that stores Enedis's Linky daily power consumption to InfluxDB.

## Image building

```
docker build -t barasher/linky-to-influxdb:latest .
```

## Execution

```
docker run --rm -it
  --env LTI_LINKY_USER=[Enedis login]
  --env LTI_LINKY_PASS=[Enedis password]
  --env LTI_IDB_URL=[InfluxDB URL]
  --env LTI_IDB_DB=[InfluxDB database]
  --env LTI_IDB_LOC=[Localisation]
  barasher/linky-to-influxdb:latest
```

Environment variables :
- **LTI_LINKY_USER**: Enedis account login, required
- **LTI_LINKY_PASS**: Enedis account password, required
- **LTI_IDB_URL**: InfluxDB URL, required (ex : http://192.168.0.2:8086)
- **LTI_IDB_DB**: InfluxDB database, required
- **LTI_IDB_LOC**: Location, required (No space and special character)