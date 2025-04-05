# Práctico 2: Git y GitHub [Luciano Aguirre]

## 1. ¿Qué es GitHub?
GitHub es una plataforma en línea que permite a los desarrolladores almacenar, administrar y colaborar en proyectos de software utilizando el sistema de control de versiones Git.

## 2. ¿Cómo crear un repositorio en GitHub?
Luego de iniciar sesión en GitHub, haz clic en `New`, asigna un nombre al repositorio y luego haz clic en `Create repository`.

## 3. ¿Cómo crear una rama en Git?
Para crear una rama en Git, utiliza:
```bash
git branch new_branch
```

## 4. ¿Cómo cambiar a una rama en Git?
Para cambiar a una rama en Git, utiliza:
```bash
git checkout new_branch
```
Desde la versión v2.23.0 también puedes utilizar:
```bash
git switch new_branch
```

## 5. ¿Cómo fusionar ramas en Git?
Para fusionar ramas en Git:
```bash
git merge main
```
Por ejemplo, desde la rama `release/latest` ejecuta:
```bash
git checkout release/latest
git merge main
```

## 6. ¿Cómo crear un commit en Git?
Para crear un commit, primero agrega los cambios:
```bash
git add .                # Todos los archivos
git add readme.md        # Archivo específico
```
Luego crea el commit:
```bash
git commit -m 'feat: new readme'
```

## 7. ¿Cómo enviar un commit a GitHub?
Para enviar un commit a GitHub:
```bash
git push origin <branch>
```

## 8. ¿Qué es un repositorio remoto?
Un repositorio remoto es una versión alojada en línea (GitHub, GitLab, etc.) que permite compartir código, colaborar y realizar copias de seguridad.

## 9. ¿Cómo agregar un repositorio remoto a Git?
Para agregar un repositorio remoto:
```bash
git remote add origin <URL>
```

## 10. ¿Cómo empujar cambios a un repositorio remoto?
Para empujar (push) cambios:
```bash
git push origin <branch>
```

## 11. ¿Cómo tirar de cambios de un repositorio remoto?
Puedes usar:
- Para traer y fusionar automáticamente:
```bash
git pull origin <branch>
```
- Para traer cambios sin fusionar:
```bash
git fetch origin <branch>
```

## 12. ¿Qué es un fork de repositorio?
Un fork es una copia personal de un repositorio externo en tu cuenta, permitiendo modificaciones sin afectar el original.

## 13. ¿Cómo crear un fork de un repositorio?
En GitHub, visita el repositorio, haz clic en `Fork`, asigna un nombre y confirma con `Create fork`.

## 14. ¿Cómo enviar una solicitud de extracción (pull request)?
Sube tus cambios a GitHub y luego selecciona la opción para crear un pull request, describiendo los cambios realizados.

## 15. ¿Cómo aceptar una solicitud de extracción?
Haz clic en `Merge Pull Request` en GitHub.

## 16. ¿Qué es una etiqueta en Git?
Una etiqueta (tag) marca puntos específicos en el historial del repositorio.

## 17. ¿Cómo crear una etiqueta en Git?
```bash
git tag <nombre_etiqueta>
```

## 18. ¿Cómo enviar una etiqueta a GitHub?
Para enviar una etiqueta específica:
```bash
git push origin <nombre_etiqueta>
```
Para enviar todas:
```bash
git push origin --tags
```

## 19. ¿Qué es un historial de Git?
Es un registro cronológico de todos los cambios realizados en un repositorio.

## 20. ¿Cómo ver el historial de Git?
```bash
git log
```

## 21. ¿Cómo buscar en el historial de Git?
- Por palabras clave:
```bash
git log --grep="palabra clave"
```
- Por autor:
```bash
git log --author="nombre"
```
- Por fecha:
```bash
git log --since="fecha" --until="fecha"
```
- Por contenido:
```bash
git log -S"texto"
```
- Por archivo:
```bash
git log <nombre_archivo>
```

Puedes combinar estas opciones para búsquedas más específicas.

## 22. ¿Cómo borrar el historial de Git?
El historial no se elimina, sino que se reescribe con:
```bash
git rebase -i
```

## 23. ¿Qué es un repositorio privado en GitHub?
Un repositorio privado es accesible solo por personas invitadas explícitamente.

## 24. ¿Cómo crear un repositorio privado en GitHub?
Al crear el repositorio, selecciona la opción `Privado`.

## 25. ¿Cómo invitar a alguien a un repositorio privado?
Ve a `Settings > Collaborators > Add people` y busca por username, full name o email.

## 26. ¿Qué es un repositorio público en GitHub?
Un repositorio público es accesible para cualquier usuario, permitiendo ver, clonar y contribuir.

## 27. ¿Cómo crear un repositorio público?
Selecciona la opción `Public` al crear el repositorio.

## 28. ¿Cómo compartir un repositorio público?
Comparte simplemente el enlace del repositorio.

---

## Consigna 2:
- Crear un repositorio público.
- Inicializar con un archivo.

[Repositorio creado](https://github.com/lucianoaguirreee/mi-primer-repo)

### Agregar un archivo:
- Crear archivo `mi-archivo.txt`
```bash
git add .
git commit -m 'Agregando mi-archivo.txt'
git push origin main
```
[Repositorio actualizado](https://github.com/lucianoaguirreee/mi-primer-repo)

---

## Consigna 3:
[Ejercicio de conflictos](https://github.com/lucianoaguirreee/conflict-exercise)

