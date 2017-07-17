class Box {
    private:
        int l, b, h;

    public:
        Box() {
            l = 0;
            b = 0;
            h = 0;
        }

        Box(int length, int breadth, int height) {
            l = length;
            b = breadth;
            h = height;
        }

        int getLength() {
            return l;
        }

        int getBreadth() {
            return b;
        }

        int getHeight() {
            return h;
        }

        long long CalculateVolume() {

            return 1LL * l * b * h;
        }

        bool operator <(Box &box) {
            bool less = false;
            if (l < box.getLength()) {
                less = true;
            }
            if ((b < box.getBreadth()) && (l == box.getLength())) {
                less = true;
            }
            if ((h < box.getHeight()) && (l == box.getLength()) && (b == box.getBreadth()) ) {
                less = true;
            }
            return less;
        }

        friend std::ostream& operator<< (std::ostream& stream, const Box& box) {
            stream << box.l << " " << box.b << " " << box.h;
            return stream;
        }
};
