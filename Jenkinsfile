pipeline {
   agent any
   stages {
      stage('test') {
         steps {
            browserstack(credentialsId: 'b787b27e-a626-49d2-a83c-8a80556e97f1') {
                sh 'pip install -r requirements.txt'
                sh 'cd android'
                sh 'browserstack-sdk pytest test5android.py'
                sh 'cd ios'
                sh 'browserstack-sdk pytest test5ios.py'
               //  sh './BrowserStackLocal --key $BROWSERSTACK_ACCESS_KEY --daemon stop'
		
		// Enable reporting in Jenkins
             	// browserStackReportPublisher 'app-automate'
            }
         }
      }
    }
  }