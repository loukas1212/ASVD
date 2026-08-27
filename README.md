# Another Simple Video Download (v0.2)

## (Ceci est le reupload d'un ancien projet, le projet n'est pas complet et les mises à jour arriveront lentement)

Un script prévu pour simplifier l'usage de YT-DLP.

Le script permet actuellement de télécharger uniquement des **vidéos**. Je compte ajouter le support des fichiers audio plus tard (~~quand j'aurai pas la flemme mdr~~).

---

Le script nécessite les dépendances suivantes :

`yt-dlp`, `colorama` et `tqdm`

Vous pouvez les installer facilement dans un environnement virtuel (VENV) avec la commande suivante :

```text
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Ou, pour Windows :

```text
python3 -m venv venv
source venv\Scripts\activate
pip install -r requirements.txt
```

Vous pouvez également installer les paquets sur l'ensemble du système (non recommandé) avec :

```text
pip install -r requirements.txt --break-system-packages
```

---

(!!! Information importante !!! : Ce script est testé sur **macOS (26.6.2)** ; même si normalement le script devrait fonctionner sur tous les OS, je ne peux pas assurer la compatibilité.)