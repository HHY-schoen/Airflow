
- **安裝Airflow**
    - 安裝指令如下
        - pip install "apache-airflow[virtualenv,rabbitmq,celery,postgres]==2.7.3" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.7.3/constraints-3.8.txt"
        > 若需要額外安裝所需套件，如Airflow連線資料庫的connector(或driver)，請詳見 Documentation 


- **設定Airflow**
    - 以下在airflow/airflow.cfg的各個block之中，需要修改的項目
    ```python
    [core]
    dags_folder
    # 讀取dag的資料夾所在處
    default_timezone
    # Airflow本身的時區設定
    executor
    # 執行器設定，會因單機執行或分散式執行而有設定差異

    [database]
    sql_alchemy_conn
    # 資料庫連線字串，Airflow所有核心資訊、狀態皆儲存於此
    sql_engine_encoding
    # 資料庫引擎編碼

    [webserver]
    base_url
    # http://<IP>/<base_url>，可配合nginx的reverse proxy
    default_ui_timezone
    # Airflow UI的時區設定
    web_server_host
    # Aairflow平台的host設定
    ```

- **資料初始化**
    - 資料庫的連線資訊設定完畢後，新建Airflow專用資料庫與資料初始化
    ```bash
    airflow db migrate
    airflow users create \
        --username admin \
        --firstname Peter \
        --lastname Parker \
        --role Admin \
        --email spiderman@superhero.org
    ```

- **啟動服務**
    - airflow scheduler
    - airflow webserver --port 8080


- **常用腳本**
    - 排程器與網頁服務
    ```python
    # 排程器執行腳本
    # bash run_airflow_scheduler.sh
    # 腳本檔備份位置: /mnt/shared/servers/crawler/airflow/run_airflow_scheduler.sh
    # 或可用以下指令執行
    sudo service airflow-scheduler start|stop|restart|...
    # 網頁服務執行腳本
    # bash run_airflow_webserver.sh
    # 腳本檔備份位置: /mnt/shared/servers/crawler/airflow/run_airflow_webserver.sh
    # 或可用以下指令執行
    sudo service airflow-webserver start|stop|restart|...
    ```

    - 更新Airflow (liontk or crawler)
    ```python
    # Airflow更新執行腳本
    # 腳本檔備份位置: /mnt/shared/servers/crawler/airflow/run_airflow_update.sh
    bash run_airflow_update.sh
    ```

- **資料庫資訊**
    - 目前Airflow的metadata皆存放於postgreSQL，database名稱為airflow-external
