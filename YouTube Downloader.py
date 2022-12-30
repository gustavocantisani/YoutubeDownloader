from pytube import YouTube


def Download(link):
  youtube_object = YouTube(link)
  youtube_object = youtube_object.streams.get_highest_resolution()
  try:
    youtube_object.download()
  except:
    print("Houve um erro ao tentar realizar o download desse vídeo.")
  print("O download do vídeo foi realizado com sucesso!")


link = input("Insira o link do YouTube para download. URL: ")
Download(link)
