include .env
# Directorio que contiene los manifiestos
MANIFEST_DIR := ci/k8s

# Obtiene la lista de archivos YAML en el directorio de manifiestos
MANIFESTS := $(wildcard $(MANIFEST_DIR)/*.yaml)

.PHONY: deploy apply delete

# Regla para desplegar los manifiestos
deploy: build-image minikube-docker-env
	kubectl apply -f $(MANIFEST_DIR)
	kubectl config set-context minikube --namespace=$(NAMESPACE)
	@echo "_________DEPLOY__________"
	kubectl get pods

# Regla para aplicar los manifiestos
apply: minikube-docker-env

	kubectl apply -f $(MANIFEST_DIR)
	kubectl config set-context minikube --namespace=$(NAMESPACE)
	@echo "_________APPLY__________"
	kubectl get pods

# Regla para eliminar los recursos de Kubernetes
delete:
	kubectl delete -f $(MANIFEST_DIR) --ignore-not-found=true
	@echo "_________DELETE__________"
	kubectl get pods

build-image:
	@echo "_________ BUILD IMAGE __________"
	docker build -t $(IMAGE_NAME) .

# Regla para configurar el entorno Docker de Minikube
minikube-docker-env:
	eval $$(minikube docker-env)
