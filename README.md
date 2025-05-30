# Projet-Docker-Kubernetes
Partie 1 : Docker
	•	Écrire un Dockerfile pour le backend Flask
	•	Écrire un Dockerfile pour le frontend React
	•	Créer un réseau docker-compose.yml si tu veux tester localement hors Kubernetes


 Partie 2 : Kubernetes
	•	Créer les fichiers YAML suivants :
	•	backend-deployment.yaml et backend-service.yaml
	•	frontend-deployment.yaml et frontend-service.yaml
	•	db-deployment.yaml et db-service.yaml
	•	secret.yaml pour les credentials PostgreSQL
	•	configmap.yaml pour les variables d’environnement (facultatif)
	•	Ajouter un Ingress Controller (optionnel) pour un accès via nom de domaine local

 Partie 3 : Visualisation et vérification
	•	Déployer le Dashboard Kubernetes (minikube dashboard)
	•	Vérifier que tous les pods sont en état Running
	•	Vérifier que le frontend communique bien avec le backend
	•	Vérifier que le backend communique bien avec PostgreSQL

Points de plus:
Ajouter monitoring (Prometheus/Grafana)
Déployer le projet sur AKS

Rendu:
  • un fichier zip qui contient tout le projet fonctionnel avec les fichiers à remplir.
  • Les urls des images du backend et du frontend sur votre dockerhub 
