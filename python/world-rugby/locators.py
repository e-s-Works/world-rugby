from selenium.webdriver.common.by import By

class CookieSettingPageLocators(object):
	REFUSE_COOKIE_BUTTON = (By.XPATH, '//*[text() = "全てのクッキーを拒否する"]')

class ManRankingPageLocators(object):
	__RANKING_TABLE_CONTAINER = '//*[@class="wr-table"][@data-sport-type="mru"]'
	SHOW_FULL_TABLE_BUTTON = (By.XPATH, f'{__RANKING_TABLE_CONTAINER}//*[@class="wr-table__button-container"]//*[ normalize-space( string() ) = "Show Full Table" ]')

	__RANKING_TABLE = f'{__RANKING_TABLE_CONTAINER}//*[@class="wr-table__table"]'
	__HEADER_ROW    = f'{__RANKING_TABLE}//*[@class="wr-table__table-header"]'
	TEAM_HEADER  = (By.XPATH, f'{__HEADER_ROW}//*[ contains( concat( " ", normalize-space(@class) ), " wr-table__header-cell--team" ) ]')
	RANK_HEADER  = (By.XPATH, f'{__HEADER_ROW}//*[ contains( concat( " ", normalize-space(@class) ), " wr-table__header-cell--position" ) ]//*[@class="u-hide-tablet"]')
	POINT_HEADER = (By.XPATH, f'{__HEADER_ROW}//*[ contains( concat( " ", normalize-space(@class) ), " wr-table__header-cell--points" ) ]//*[@class="u-hide-tablet"]')
	
	__RANKING_TABLE_BODY             = f'{__RANKING_TABLE}//tbody'
	__RANKING_TABLE_ROWS             = f'{__RANKING_TABLE_BODY}//*[ contains( concat( normalize-space(@class), " " ), "wr-table__table-row " ) ]'
	__RANKING_TABLE_TEAM_NAME_COLUMN = f'{__RANKING_TABLE_ROWS}//*[ contains( concat( " ", normalize-space(@class) ), " wr-table__cell--team" ) ]'
	__JAPAN_ROW                      = f'{__RANKING_TABLE_TEAM_NAME_COLUMN}[ contains( normalize-space( string() ), "日本" ) ]/..'
	JAPAN_ROW       = (By.XPATH, __JAPAN_ROW)
	JAPAN_TEAM_NAME = (By.XPATH, f'{__JAPAN_ROW}//*[ contains( concat( " ", normalize-space(@class) ), " wr-table__cell--team" ) ]')
	JAPAN_RANK      = (By.XPATH, f'{__JAPAN_ROW}//*[ contains( concat( " ", normalize-space(@class) ), " wr-table__cell--position" ) ]')
	JAPAN_PREV_RANK = (By.XPATH, f'{__JAPAN_ROW}//*[@class="wr-table__last-position"]')
	JAPAN_POINT     = (By.XPATH, f'{__JAPAN_ROW}//*[ contains( concat( " ", normalize-space(@class) ), " wr-table__cell--points" ) ]')

	__YEAR_SELECT_BOX = '.js-year-button'
	SELECTED_YEAR = (By.CSS_SELECTOR, f'{__YEAR_SELECT_BOX} .wr-datepicker__selected')

	__DATE_SELECT_BOX = '.js-week-button'
	DATE_SELECT_BOX   = (By.CSS_SELECTOR, __DATE_SELECT_BOX)
	SELECTED_DATE     = (By.CSS_SELECTOR, f'{__DATE_SELECT_BOX} .wr-datepicker__selected')
	DATE_SELECT_ITEMS = (By.CSS_SELECTOR, f'{__DATE_SELECT_BOX} .wr-datepicker__option-label')

class OutputPageLocators(object):
	HTML = (By.TAG_NAME, 'html')

	DATA_YEAR = (By.ID, 'year')
	DATA_TEAM = (By.ID, 'team')
	
	TABLE_HEADER      = (By.TAG_NAME, 'thead')

	__TABLE_BODY = '//tbody'
	TABLE_BODY = (By.XPATH, __TABLE_BODY)
	FIRST_ROW  = (By.XPATH, f'{__TABLE_BODY}//tr[1]')
	DATA_ROWS  = (By.XPATH, f'{__TABLE_BODY}//tr')