#include <iostream>
 
class A {
public:
    A() : m_num(0) {}
    explicit A(int i) {
        m_num = i * 2;
    }
    A& operator=(int i) {
        m_num = i;
        return *this;
    }
    int m_num;
};
 
int main(void) {
    A a1(10);      // コピーコンストラクタが呼ばれて20になってほしい
    A a2 = 10;     // 代入演算子が呼ばれて10になってほしい ※間違い！
    A a3; a3 = 10; // 代入演算子が呼ばれて10になってほしい
    std::cout << "a1:" << a1.m_num << std::endl; // 期待通り20
    std::cout << "a2:" << a2.m_num << std::endl; // 期待に反して20
    std::cout << "a3:" << a3.m_num << std::endl; // 期待通り10
}
