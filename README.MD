# Linky to InfluxDB

**Linky to InfluxDB** is a Docker image that stores Enedis's Linky daily power consumption to [InfluxDB](https://docs.influxdata.com/influxdb/).

With a [Chronograf](https://www.influxdata.com/time-series-platform/chronograf/) or a [Grafana](https://grafana.com/) connected to the InfluxDB database, such representations will be possible :

![Chronograf](chronografLinky.png)

## Principles

- Linky data is gathered using [Pylinky](https://github.com/Pirionfr/pyLinky)
- Pylinky data is converted to [InfluxDB line protocol](https://docs.influxdata.com/influxdb/v1.7/write_protocols/line_protocol_tutorial/)
- [influxdb-pusher](https://github.com/barasher/influxdb-pusher) is used to push converted data to InfluxDB

## Docker image

### Image retrieving

```
docker pull barasher/linky-to-influxdb:[tag]
```

- **[version]** : linux 386 version, sample : `barasher/linky-to-influxdb:1.3.1`
- **[version]-armv7** : armv7 version (raspberry pi, ...), sample : `barasher/linky-to-influxdb:1.3.1-armv7` 


### Image building
 
```
docker build -t barasher/linky-to-influxdb:latest .
```

## Execution

Environment variables :
- **LTI_LINKY_USER**: Enedis account login, required
- **LTI_LINKY_PASS**: Enedis account password, required
- **LTI_IDB_URL**: InfluxDB URL, required (ex : http://192.168.0.2:8086)
- **LTI_IDB_DB**: InfluxDB database, required
- **LTI_IDB_LOC**: Location, required (No space and special character)

### Retrieve yesterday's data

```
docker run --rm
  --env LTI_LINKY_USER=[Enedis login]
  --env LTI_LINKY_PASS=[Enedis password]
  --env LTI_IDB_URL=[InfluxDB URL]
  --env LTI_IDB_DB=[InfluxDB database]
  --env LTI_IDB_LOC=[Localisation]
  barasher/linky-to-influxdb:latest
```

### Retrieve specific period data

```
docker run --rm
  --env LTI_LINKY_USER=[Enedis login]
  --env LTI_LINKY_PASS=[Enedis password]
  --env LTI_IDB_URL=[InfluxDB URL]
  --env LTI_IDB_DB=[InfluxDB database]
  --env LTI_IDB_LOC=[Localisation]
  barasher/linky-to-influxdb:latest ./recover.sh [first date (format dd/mm/yyyy)] [how many days]
```

To retrieve data concerning the 31st of December 2018, here is the full command line :

```
docker run --rm 
  --env LTI_LINKY_USER=[Enedis login]
  --env LTI_LINKY_PASS=[Enedis password]
  --env LTI_IDB_URL=[InfluxDB URL]
  --env LTI_IDB_DB=[InfluxDB database]
  --env LTI_IDB_LOC=[Localisation]
  barasher/linky-to-influxdb:latest ./recover.sh 31/12/2018 1
```

To retrieve data concerning 12 days from the 1st of February 2018 (included), here is the full command line :

```
docker run --rm 
  --env LTI_LINKY_USER=[Enedis login]
  --env LTI_LINKY_PASS=[Enedis password]
  --env LTI_IDB_URL=[InfluxDB URL]
  --env LTI_IDB_DB=[InfluxDB database]
  --env LTI_IDB_LOC=[Localisation]
  barasher/linky-to-influxdb:latest ./recover.sh 01/02/2018 12
```

## Changelog

- [v1.3](https://github.com/barasher/linky-to-influxdb/milestone/3)
  - [Add secure password management](https://github.com/barasher/linky-to-influxdb/pull/7) thanks to @roondar
- [v1.3.1](https://github.com/barasher/linky-to-influxdb/milestone/4)
  - [Better error logging](https://github.com/barasher/linky-to-influxdb/pull/9) thanks to @roondar
