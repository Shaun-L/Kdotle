
class SongAt:

  def __init__(self, title, album, pos, length, feature):
    self._title = title
    self._album = album
    self._pos = pos
    self._length = length
    self._feature = feature


  @property
  def title(self):
    return self._title

  @property
  def album(self):
    return self._album

  @property
  def pos(self):
    return self._pos

  @property
  def length(self):
    return self._length

  @property
  def feature(self):
    return self._feature

  

  