# 🌤️ MriduManda

**MriduManda** is a lightweight Python application that fetches real-time weather data for any city using the OpenWeatherMap API. Designed with simplicity and clean structure in mind, the app offers a minimal but effective interface for accessing weather insights from the command line or future integrations.

---

## 🚀 Features

- 🔍 Fetch current weather by city name
- 🌡️ Displays temperature and condition
- 🌆 Automatic City detection

---

## 📦 Tech Stack

- Python 3.10+
- [Requests](https://pypi.org/project/requests/) for HTTP communication
- JSON for data handling
- Poetry for dependency management
- [Rich](https://pypi.org/project/rich/) for Beautiful Weather Disclosure

---

## 🛠️ Usage

For automatic city detection

```
poetry run mrdmnd
```
For manual city enter
```
poetry run mrdmnd -m
```

## 🎑 Presentation 

- Default --- ```just press enter or 'd' when asked for weather print options```

![Default weather presentation](assets/default.png)


- OneLiner --- ```enter 'o' when asked for weather print options```

![OneLiner weather presentation](assets/oneliner.png)



- Formatted --- ```enter 'f' when asked for weather print options```

![Formatted weather presentation](assets/formatted.png)


- Formatted OneLiner --- ```enter 'fo' when asked for weather print options```

![Formatted OneLiner weather presentation](assets/formatted-oneliner.png)


- Ascii --- ```enter 'a' when asked for weather print options```

![Weather presentation with Ascii Arts](assets/ascii.png)


## Attributions

Like the original version of mine, this version also uses the ASCII art for weather representation. These representations (ASCII arts) were created by [Julynx](https://github.com/Julynx). It was taken from [here](https://github.com/Julynx/wthr).


## 📝 Changelog

# Version 1.0.5 (Latest release)
- Refactored the code to improve performance
- Miscellaneous code improvements
- Improved ```README.md```

The complete [changelog](https://github.com/padm3-sh/mridumanda/blob/main/LOG.md) can be found here.

## 📍 Note

This project is a rewritten version of the original MriduManda, which was developed under another GitHub account of mine in [this](https://github.com/shvedt/mridu-manda.git) repo. That account is no longer accessible, and as a result, the project is being completely rebuilt here from scratch — keeping its original purpose, but with improved clarity, structure, and maintainability.

