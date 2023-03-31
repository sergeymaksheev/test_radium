# test_radium
Тестовое задание:

Напишите скрипт, асинхронно, в 3 одновременных задачи, скачивающий содержимое HEAD репозитория https://gitea.radium.group/radium/project-configuration во временную папку.

После выполнения всех асинхронных задач скрипт должен посчитать sha256 хэши от каждого файла.

Код должен проходить без замечаний проверку линтером wemake-python-styleguide. Конфигурация nitpick - https://gitea.radium.group/radium/project-configuration

Обязательно 100% покрытие тестами

При выполнении в ChatGPT - обязательна переработка


NB!!! Перед запуском необходимо установить переменную окружения со значением:
GIT_REPO_URL=https://gitea.radium.group/radium/project-configuration.git


![Build status][(https://github.com/sergeymaksheev/test_radium/actions/workflows/testing.yml/badge.svg?branch=main)]
(https://github.com/sergeymaksheev/test_radium/actions/workflows/testing.yml)