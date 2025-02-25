# Breakfast-order-system
順哥廚房早餐店點餐系統

Base on Django Web application, Demo 早餐店的購物車和結帳系統。

(Note:順哥廚房早餐店已經有自己的線上點餐系統，有興趣的可以進到[順哥廚房臉書](https://www.facebook.com/kevin09140711)查看)



https://github.com/user-attachments/assets/58af859f-b8bd-487e-bbeb-23c32093ab53








## 安裝與使用

1. 克隆此專案到本地端：
    ```sh
    git clone https://github.com/你的帳號/你的專案.git
    cd 你的專案
    ```

2. 建立並啟動虛擬環境：
    ```sh
    python -m venv env
    source env/bin/activate  # 對於 Windows 使用者，請使用 `env\Scripts\activate`
    ```

3. 安裝所需套件：
    ```sh
    pip install -r requirements.txt
    ```

4. 進行資料庫遷移：
    ```sh
    python manage.py migrate
    ```

5. 啟動開發伺服器：
    ```sh
    python manage.py runserver
    ```

6. 在瀏覽器中打開 [http://127.0.0.1:8000/](http://_vscodecontentref_/19) 來查看應用程式。

## 功能

- 瀏覽早餐店菜單
- 添加商品到購物車
- 查看購物車總覽
- 結帳並提交訂單
- 查看結帳確認頁面

## 目錄結構說明

- [myapp](http://_vscodecontentref_/20)：主要的應用程式目錄，包含了模型、視圖、模板等。
- [myproject](http://_vscodecontentref_/21)：專案的設定目錄，包含了設定檔、URL 配置等。
- `static/`：靜態檔案目錄，包含了 CSS 樣式表。
- `templates/`：模板目錄，包含了 HTML 模板檔案。


