# Lending-Club---Credit-Risk-Analysis-Models

Secara umum, project ini terbagi menjadi 4 bagian utama yang membutuhkan beberapa file masing-masingnya. Adapun 3 bagian itu adalah:
1.	Data

•	loan
project ini menggunakan raw data yang bersumber dari https://www.kaggle.com/janiobachmann/lending-club-risk-analysis-and-metrics/data. Karena file yang digunakan memliki size yang besar sehingga data yang ada perlu di partisi menjadi 4 bagian yakni loan.part01 hingga loan.part04.

•	cleandata_loan_test4
cleandata_loan_test4 ini merupakan hasil modifikasi dari raw data yang sudah melalui tahapan missing handling value sehingga data tidak ada null value. Karena file yang digunakan memliki size yang besar sehingga data yang ada perlu di partisi menjadi 2 bagian yakni cleandata_loan_test4.part01 dan cleandata_loan_test4.part02


•	cleanVIF_loan_test4
setelah data dilengkapi, kemudian dilakukan multicollinearity checking dari setiap feature. Dari tahapan tersebut, jumlah feature tersebut telah di reduce dan siap untuk tahap selanjutnya.


2.	Jupyter Notebook

•	Data Preparation & EDA
	Tahapan ini menggunakan data loan mulai dari part 01 hingga part 04. Pada tahapan ini, terdapat analisa data awal yang dapat menggambarkan business process dari Lending Club. Analisa awal ini dapat membantu researcher untuk mengetahui secara utuh semua feature yang ada dan menjadi informasi tambahan pada analisa selanjutnya. Dari jupyter notebook ini di export cleandata_loan_test4

•	Pre-modelling
	Tahapan ini menggunakan data cleandata_loan_test4, dimana pada tahapan ini dilakukan analisa terhadap distribusi yang dipisah berdasarkan target klasifikasi. Selain itu dari data ini juga dilakukan reduksi feature yang significant dan tidak ada multicolinnearity tiap feature nya. Dari tahapan ini dihasilkan data yang sudah tereduksi feature yakni cleanVIF_loan_test4.

•	Model 1 - Logistic Regression
	Tahapan ini menggunakan data cleanVIF_loan_test4, dan menggunakan model Logistic Regression. Pada model logistic regression ini data yang ada menggunakan normal data dan oversampling data. Dari 2 tipe data tersebut dilakukan evaluasi modelnya menggunakan confusion matrix.

•	Model 2 - Random Forest
	Tahapan ini menggunakan data cleanVIF_loan_test4, dan menggunakan model Random Forest. Pada model random forest ini dilakukan 3 test menggunakan model random forest dengan 3 parameter yang berbeda. Dari 3 parameter tersebut dilakukan evaluasi modelnya menggunakan confusion matrix pada masing-masing testnya

•	Model 3 - XGBoost
	Tahapan ini menggunakan data cleanVIF_loan_test4, dan menggunakan model XGBoost. Pada model XGBoost ini dilakukan data yang ada menggunakan normal data, oversampling data dan PCA. Dari masing-masing tes tersebut dilakukan evaluasi menggunakan confusion matrix.

3.	Dashboard

Dari analisa data dan model yang ada, di susun Dash_LendingClub yang terdiri dari 3 bagian yakni Highlight, Loan Statistic dan Calculate Customer Credit Risk. Bagian Highlight, dapat dianalisa deskripsi dan pertumbuhan bisnis Lending Club serta distribusi persebaran jumlah pinjaman yang sudah diberikan. Pada bagian Loan Statistic dapat dilihat perbedaan distribusi tiap feature data yang dibedakan menjadi 2 kategori berdasarkan targetnya yakni Good Loan atau Bad Loan.  Dan pada bagian Calculate Customer Credit Risk, dapat dianalisa pada data baru mengenai risiko kredit dari customer yang ingin melakukan pinjaman pada Lending Club.

4.	Deck presentasi

Pada file Lending Club - Loan Credit Risk, merupakan deck presentasi untuk project ini yang berisi gambaran secara umum serta ringkasan bagaimana project ini dijalankan.
