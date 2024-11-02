pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                // Instala as dependências listadas no arquivo requirements.txt
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Executa os testes usando pytest e limita falhas a 1 para feedback rápido
                sh 'pytest --maxfail=1 --disable-warnings'
            }
        }
    }

    post {
        success {
            echo "Todos os testes passaram! ✅"
        }
        failure {
            echo "Alguns testes falharam. ⚠️"
        }
    }
}
.
