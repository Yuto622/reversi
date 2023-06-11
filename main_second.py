import pandas as pd
import numpy as np

#ボードをデータフレームで作成する関数
def make_board_df() -> pd.DataFrame:
   

  board_df = pd.DataFrame(
                        columns=["A", "B", "C", "D", "E", "F", "G", "H"],
                        index=["1", "2", "3", "4", "5", "6", "7", "8"])

    
  return board_df
board_df = make_board_df()
print(board_df)

#0の駒をおく関数
def place_a_piece_0(board_df: pd.DataFrame) -> pd.DataFrame:
    question_where_to_place_index = input("どこにおきたいですか")
    question_where_to_place_collum = input("どこにおきたいですか")
    board_df.loc[question_where_to_place_index, question_where_to_place_collum] = 0
    return board_df

#1の駒をおく関数
def place_a_piece_1(board_df: pd.DataFrame) -> pd.DataFrame:
    question_where_to_place_index = input("どこにおきたいですか")
    question_where_to_place_collum = input("どこにおきたいですか")
    board_df.loc[question_where_to_place_index, question_where_to_place_collum] = 1
    return board_df


board_df = place_a_piece_0(board_df)

print(board_df)

board_df = place_a_piece_1(board_df)

print(board_df)

# CSVファイルに吐き出して盤を保存する関数
def board_df_to_csv(board_df: pd.DataFrame):
    board_df = board_df.to_csv("board.csv", index = False)
    return board_df
board_df_to_csv(board_df)

#作成したcsvファイルを読み込んで出力
def read_csv_with_correct_index(board_df: pd.DataFrame):  
  board_df = pd.read_csv("board.csv")
  board_df.index = index = ["1", "2", "3", "4", "5", "6", "7", "8"]

  return board_df

print(board_df)

#64ます全ての座標を提供する関数
def provide_all_places(board_df: pd.DataFrame) -> list:
    index = ["1", "2", "3", "4", "5", "6", "7", "8"]
    columns= ["A", "B", "C", "D", "E", "F", "G", "H"]
    
    all_places_list = []
    for i in index:
        for column in columns:
          all_places_list.append([i, column])
    return all_places_list

all_places_list =  provide_all_places(board_df)
print(all_places_list)

#空白であることを確認する関数
def check_if_empty(board_df: pd.DataFrame, all_places_list: list) -> list:
    posibble_place_list = []

    # すべてのマス目を調べる
    for place in all_places_list:
        index_of_place = place[0]
        column_of_place = place[1]
        print(index_of_place, column_of_place)
        # そのマス目が空白かどうかを確認
        print(board_df.loc[index_of_place,column_of_place])

        if pd.isnull(board_df.loc[index_of_place,column_of_place]):
          posibble_place_list.append([index_of_place,column_of_place])
    return posibble_place_list
   
posibble_place_list = check_if_empty(board_df, all_places_list)
print(posibble_place_list)

#同じ色が連続しているか探索する関数（右）
def explore_right_direction(board_df: pd.DataFrame, posibble_place_list: list) -> list:
  right_possible_list = []

  for possible_place in posibble_place_list:
    i = possible_place[0]
    column = possible_place[1]

    columns= ["A", "B", "C", "D", "E", "F", "G", "H"]

    #今探索する座標のカラムのインデックス番号
    place_now = columns.index(column)
    try:
      #そのインデクス番号に１を足して、一個右からのポイントを取得
      next_column = columns[place_now + 1]
    #取得した位置から右方向のシリーズを作成
      series_from_specific_point = board_df.loc[i, next_column:"H"]
      #そのシリーズに入っている値が同じである場合、ユニーク。また、nanでないことを判定.欠損値でないときにTrueを返すように、numpyを使用してから結果を反転
      if (len(series_from_specific_point.unique()) == 1) and not(np.isnan(series_from_specific_point.loc[next_column])):
         right_possible_list.append([i, column])
         
    except IndexError as error:
      pass

  return right_possible_list

right_possible_list = explore_right_direction(board_df, posibble_place_list)
print(right_possible_list)

#同じ色が連続しているか探索する関数（左）
def explore_left_direction(board_df: pd.DataFrame, posibble_place_list: list) -> list:
  left_possible_list = []

  for possible_place in posibble_place_list:
    i = possible_place[0]
    column = possible_place[1]

    columns= ["A", "B", "C", "D", "E", "F", "G", "H"]

    #今探索する座標のカラムのインデックス番号
    place_now = columns.index(column)
    try:
      #そのインデクス番号に１を引いて、一個左からのポイントを取得
      next_column = columns[place_now - 1]
    #取得した位置から左方向のシリーズを作成
      series_from_specific_point = board_df.loc[i, "A":next_column]
      #そのシリーズに入っている値が同じである場合、ユニーク。また、nanでないことを判定.欠損値でないときにTrueを返すように、numpyを使用してから結果を反転
      if (len(series_from_specific_point.unique()) == 1) and not(np.isnan(series_from_specific_point.loc[next_column])):
         left_possible_list.append([i, column])
         
    except IndexError as error:
      pass

  return left_possible_list

left_possible_list = explore_left_direction(board_df, posibble_place_list)
print(left_possible_list)

#同じ色が連続しているか探索する関数（上）
def explore_up_direction(board_df: pd.DataFrame, posibble_place_list: list) -> list:
  up_possible_list = []

  for possible_place in posibble_place_list:
    i = possible_place[0]
    column = possible_place[1]
    index = ["1", "2", "3", "4", "5", "6", "7", "8"]
      
    #今探索する座標のインデックスのインデックスのインデックス番号
    place_now = index.index(i)
    try:
      #そのインデクス番号に１を引いて、一個上からのポイントを取得
      next_index = index[place_now - 1]
    #取得した位置から上方向のシリーズを作成
      series_from_specific_point = board_df.loc["1":next_index, column]
      #そのシリーズに入っている値が同じである場合、ユニーク。また、nanでないことを判定.欠損値でないときにTrueを返すように、numpyを使用してから結果を反転
      if (len(series_from_specific_point.unique()) == 1) and not(np.isnan(series_from_specific_point.loc[next_index])):
         left_possible_list.append([i, column])
         
    except IndexError as error:
      pass

  return up_possible_list

up_possible_list = explore_up_direction(board_df, posibble_place_list)
print(up_possible_list)

#同じ色が連続しているか探索する関数（下）
def explore_down_direction(board_df: pd.DataFrame, posibble_place_list: list) -> list:
  down_possible_list = []

  for possible_place in posibble_place_list:
    i = possible_place[0]
    column = possible_place[1]
    index = ["1", "2", "3", "4", "5", "6", "7", "8"]
      
    #今探索する座標のインデックスのインデックスのインデックス番号
    place_now = index.index(i)
    try:
      #そのインデクス番号に１を足して、一個下からのポイントを取得
      next_index = index[place_now + 1]
    #取得した位置から下方向のシリーズを作成
      series_from_specific_point = board_df.loc[next_index:"8", column]
      #そのシリーズに入っている値が同じである場合、ユニーク。また、nanでないことを判定.欠損値でないときにTrueを返すように、numpyを使用してから結果を反転
      if (len(series_from_specific_point.unique()) == 1) and not(np.isnan(series_from_specific_point.loc[next_index])):
         left_possible_list.append([i, column])
         
    except IndexError as error:
      pass

  return down_possible_list

down_possible_list = explore_up_direction(board_df, posibble_place_list)
print(down_possible_list)

#同じ色が連続しているか探索する関数（右下）
def explore_right_down_direction(board_df: pd.DataFrame, posibble_place_list: list) -> list:
  right_down_possible_list = []
  for possible_place in posibble_place_list:
    i = possible_place[0]
    column = possible_place[1]

    index = ["1", "2", "3", "4", "5", "6", "7", "8"]
    columns= ["A", "B", "C", "D", "E", "F", "G", "H"]

    try:
      #一個右下の座標を取得
      index_of_place_now = index.index(i)
      next_index = index[index_of_place_now + 1]

      column_of_place_now = columns.index(column)
      next_column = columns[column_of_place_now + 1]

      board_df_for_right_down_direction = board_df.loc[next_index:"8",  next_column:"H"]
      # データフレームをNumPyの配列に変換
      array_for_right_down_direction = board_df_for_right_down_direction.to_numpy()

      # 対角線上の要素を抽出
      diagonal_elements_for_right_down_direction = np.diagonal(array_for_right_down_direction)  

      if (len(np.unique(diagonal_elements_for_right_down_direction)) == 1) and not(np.isnan(diagonal_elements_for_right_down_direction[0])):
         right_down_possible_list.append([i, column])

      

    except IndexError as error:
       pass
    
  return right_down_possible_list

right_down_possible_list = explore_right_down_direction(board_df, posibble_place_list)
print(right_down_possible_list)

#一つのポイントを引数にとり、そこから左上の要素をシリーズでとるもの
def create_series_of_up_left(board_df: pd.DataFrame, posibble_place_list: list) -> list:

  
  index = ["1", "2", "3", "4", "5", "6", "7", "8"]
  columns = ["A", "B", "C", "D", "E", "F", "G", "H"]

  all_series_from_possible_place = []
  for possible_place in posibble_place_list:
    row = possible_place[0]
    column = possible_place[1]

    # 特定の点から左上に向かって探索
    series = []
    while index.index(row) >= 0 and columns.index(column) >= 0:
      series.append([row, column])

        # 一つ左上の座標を取得
      row_index = index.index(row)
      col_index = columns.index(column)

      if row_index == 0 or col_index == 0:
        break
      
      next_row = index[row_index - 1]
      next_col = columns[col_index - 1]

      row = next_row
      column = next_col
    
    all_series_from_possible_place.append(series)

  return all_series_from_possible_place
  
all_series_from_possible_place = create_series_of_up_left(board_df, posibble_place_list)


#左上に同じ駒が連続しているか確認する関数
def check_if_sequence(board_df: pd.DataFrame, all_series_from_possible_place):
  up_left_possible_list = []
  #点ごとに取得した、シリーズのリストから駒が連続しているか確認
  for list_of_series_from_specific_point in all_series_from_possible_place:
    if len(list_of_series_from_specific_point) >= 2:
      #始まりの点はいらないので、消す
      requires_list_of_points = list_of_series_from_specific_point[1:]
      for required_point in requires_list_of_points:
        list_of_value = []
        i = required_point[0]
        cul = required_point[1]
        value_of_required_point = board_df.loc[i, cul]
        list_of_value.append(value_of_required_point)

        #そのシリーズに入っている値が同じである場合、ユニーク。また、nanでないことを判定.欠損値でないときにTrueを返すように、numpyを使用してから結果を反転
        if (len(np.unique(list_of_value)) == 1) and not(np.isnan(list_of_value[0])):
          #連続していて、かつそれが、nanでないことが確認出来たら、置こうとしている駒の座標をアペンド
          up_left_possible_list.append(list_of_series_from_specific_point[0])

    #もし、リストに一つしか要素がなければ、左上がないということなので、探索終了
    elif len(list_of_series_from_specific_point) == 1:
      break

  return up_left_possible_list

up_left_possible_list = check_if_sequence(board_df, all_series_from_possible_place)
print(up_left_possible_list)
   
