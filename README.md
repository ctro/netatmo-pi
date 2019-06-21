# Netatmo / Pi display

You can query your local hardware with an API.
[https://dev.netatmo.com/en-US](https://dev.netatmo.com/en-US)

## Setup

- Ruby 2.5
- `bundle`
- `cp .env.example .env` and fill it out

## Tests

`ruby test/test_netatmo_info.rb`

The tests use your `.env` file and make actual API calls :)

## Weather station API 

[https://dev.netatmo.com/resources/technical/samplessdks/codesamples#getstationsdata](https://dev.netatmo.com/resources/technical/samplessdks/codesamples#getstationsdata)

## PaPiRus

https://github.com/PiSupply/PaPiRus - write a bitmap or text

## Sketch

```
In : 72°⇘  [⇓77 ⇑55] 36% 802mm📈 61db 
Out: 72°⇒  [⇓77 ⇑55] 36% 802mm⇗ 61db
```