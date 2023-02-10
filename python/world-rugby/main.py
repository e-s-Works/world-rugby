#! python3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome          import ChromeDriverManager
from page import CookieSettingPage
from page import ManRankingPage
from page import OutputPage

URL = r'https://www.world.rugby/tournaments/rankings/mru'

service = ChromeService(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
with webdriver.Chrome(service=service, options=options) as driver:
	datas = []
	driver.get(URL)

	cookie_setting_page = CookieSettingPage(driver)
	cookie_setting_page.click_refuse_btn()

	man_ranking_page = ManRankingPage(driver)
	man_ranking_page.click_show_full_table_btn()

	header_data = man_ranking_page.get_header_data()
	man_ranking_page.move_screen_to_japan_data()
	man_ranking_page.change_japan_row_background_color()
	# 最新データの日付は選択ボックスに表示されないのでここで取っておく
	data = man_ranking_page.get_japan_data()
	datas.append(data)

	man_ranking_page.click_date_select_box()
	date_items = man_ranking_page.get_date_item_values()
	man_ranking_page.click_date_select_box()
	for item in date_items:
		man_ranking_page.click_date_select_box()
		man_ranking_page.select_date(item)
		man_ranking_page.move_screen_to_japan_data()
		man_ranking_page.change_japan_row_background_color()
		data = man_ranking_page.get_japan_data()
		datas.append(data)

	datas.sort(key=lambda data: data[ManRankingPage.DATE_KEY])

	output_page = OutputPage(driver, datas)
	output_page.create_new_window()
	output_page.set_template_html()
	output_page.set_data_year()
	output_page.set_data_team()
	output_page.set_header(header_data)
	output_page.print_data_list()
	output_page.move_screen_to_first_row()
	output_page.scroll_to_last_row()
