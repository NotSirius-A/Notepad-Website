pipeline {
  agent any
  stages {
    stage("Check tools") {
      steps {
        sh '''
          docker version
          docker info
          docker compose version 
        '''
      }
    }
    stage('Prune Docker data') {
      steps {
        sh 'docker compose --env-file ./docker_compose.env down'
        sh 'docker system prune -a -f'
      }
    }
    stage('Start container') {
      steps {
        sh 'docker compose --env-file ./docker_compose.env up --build -d --wait'
        sleep(time:10, unit: "SECONDS")
        sh 'docker compose --env-file ./docker_compose.env logs'
        sh 'docker compose --env-file ./docker_compose.env ps'
      }
    }
  }
}