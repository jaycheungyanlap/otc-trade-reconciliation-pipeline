# main.py - 完整控制端
import logging
import config
from engine import run_sql_reco, apply_excel_styles
from notifier import send_reco_email

logging.basicConfig(
    filename='reco_audit.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    print(" 正在啟動自動化對帳引擎與通知管道...")
    logging.info("Reconciliation process started.")

    try:
        # 1. 對帳
        breaks = run_sql_reco(config.INTERNAL_FILE, config.BROKER_FILE)
        
        # 2. 產出 Excel 報表與美化
        breaks.to_excel(config.OUTPUT_REPORT, index=False)
        apply_excel_styles(config.OUTPUT_REPORT)
        
        # 3. 觸發郵件摘要通知 (Dry Run 模擬測試)
        send_reco_email(breaks, config.OUTPUT_REPORT, dry_run=False)
        
        logging.info(f"Process complete. Total breaks: {len(breaks)}")
        print(f" 全套流程執行完畢！Audit log 已更新。")

    except Exception as e:
        logging.error(f"Execution failed: {str(e)}")
        print(f" 執行失敗: {e}")

if __name__ == '__main__':
    main()