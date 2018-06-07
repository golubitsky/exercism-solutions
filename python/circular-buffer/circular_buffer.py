class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.clear()

    def _increment_index(self, i):
        if i + 1 < len(self.store):
            return i + 1

        return 0

    def read(self):
        if self.store[self._oldest_idx] is None:
            raise BufferEmptyException("No data to read.")

        popped, self.store[self._oldest_idx] = self.store[self._oldest_idx], None

        self._oldest_idx = self._increment_index(self._oldest_idx)

        return popped

    def write(self, data, _force=False):
        if self.store[self._cur_idx] is not None:
            if not _force:
                raise BufferFullException("Buffer full.")

        self.store[self._cur_idx] = data
        self._cur_idx = self._increment_index(self._cur_idx)

    def overwrite(self, data):
        if self.store[self._cur_idx] is not None:
            if self._cur_idx == self._oldest_idx:
                self._oldest_idx = self._increment_index(self._oldest_idx)

        self.write(data, _force=True)

    def clear(self):
        self.store = [None] * self.capacity
        self._oldest_idx = 0
        self._cur_idx = 0
