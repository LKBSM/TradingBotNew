"""
Script de monitoring pour suivre la progression en temps réel.
Génère un fichier progress.log mis à jour toutes les 30 secondes.
"""

import time
import os
from datetime import datetime

def monitor_training():
    """Affiche la progression en temps réel."""
    
    log_file = "training_progress.log"
    
    with open(log_file, 'w') as f:
        f.write(f"=== TRAINING MONITOR DÉMARRÉ ===\n")
        f.write(f"Heure: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"=" * 70 + "\n\n")
    
    print("📊 Monitoring démarré - Vérifier training_progress.log")
    
    while True:
        try:
            # Lire les dernières lignes des logs
            if os.path.exists("logs"):
                latest_log = sorted(os.listdir("logs"))[-1] if os.listdir("logs") else None
                
                if latest_log:
                    with open(f"logs/{latest_log}", 'r') as f:
                        lines = f.readlines()[-20:]  # 20 dernières lignes
                    
                    with open(log_file, 'a') as f:
                        f.write(f"\n=== UPDATE {datetime.now().strftime('%H:%M:%S')} ===\n")
                        f.writelines(lines)
            
            time.sleep(30)  # Update toutes les 30 secondes
            
        except KeyboardInterrupt:
            print("\n✅ Monitoring arrêté")
            break
        except Exception as e:
            print(f"⚠️ Erreur monitoring: {e}")
            time.sleep(30)

if __name__ == '__main__':
    monitor_training()
