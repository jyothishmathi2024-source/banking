pipeline {
    agent any

    parameters {
        choice(name: 'TRANSACTION_TYPE', choices: ['Check Balance', 'Deposit', 'Withdraw'], description: 'Select the banking operation')
        string(name: 'AMOUNT', defaultValue: '0.0', description: 'Enter the amount for Deposit or Withdrawal (Ignored for Check Balance)')
    }

    environment {
        INITIAL_BALANCE = '1000.0'
    }

    stages {
        stage('Initialize') {
            steps {
                echo 'Starting Automated Banking Transaction...'
                echo "Current base balance: ₹${env.INITIAL_BALANCE}"
            }
        }

        stage('Execute Transaction') {
            steps {
                script {
                    // Create an inline Python runner script to handle state and parameters
                    def pythonScript = """
balance = float(${env.INITIAL_BALANCE})
choice = '${params.TRANSACTION_TYPE}'
amount = float(${params.AMOUNT})

print(f"\\n--- Processing {choice} ---")

if choice == 'Check Balance':
    print(f"Current Balance: ₹{balance:.2f}")

elif choice == 'Deposit':
    if amount > 0:
        balance += amount
        print(f"Successfully deposited ₹{amount:.2f}.")
        print(f"Updated Balance: ₹{balance:.2f}")
    else:
        print("Error: Deposit amount must be positive.")
        current.result = 'FAILURE'

elif choice == 'Withdraw':
    if amount > 0:
        if balance >= amount:
            balance -= amount
            print(f"Successfully withdrew ₹{amount:.2f}.")
            print(f"Updated Balance: ₹{balance:.2f}")
        else:
            print("Error: Insufficient balance! Transaction failed.")
            error("Pipeline aborted due to insufficient funds.")
    else:
        print("Error: Withdrawal amount must be positive.")
        error("Pipeline aborted due to invalid amount.")
"""
                    // Write to file and execute via python3
                    writeFile file: 'bank_runner.py', text: pythonScript
                    sh 'python3 bank_runner.py'
                }
            }
        }
    }
}
