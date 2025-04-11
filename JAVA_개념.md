- [자바에서의 System.out.print() 줄바꿈](https://github.com/SeoMiYoung/miyoung-zone/issues/153)
- [자바 배열 초기화 기본값](https://github.com/SeoMiYoung/miyoung-zone/issues/154)
- [`=`와 `equals`](https://github.com/SeoMiYoung/miyoung-zone/issues/155)
- [오버라이딩 & 동적바인딩](https://github.com/SeoMiYoung/miyoung-zone/issues/156)
- [오버로딩](https://github.com/SeoMiYoung/miyoung-zone/issues/157)
- [추상클래스](https://github.com/SeoMiYoung/miyoung-zone/issues/159)

### ✔️ java에서의 싱글톤 패턴
클래스를 여러번 호출했을 때, 인스턴스를 하나만 생성하고, 그 다음 생성 시, 기존에 생성한 것이 있나 확인하고, 있으면 기존 것 반환 => `싱글톤`

### ✔️ swith()문
break문이 없다면, 조건을 만족한 곳~끝까지 계속 실행됨.

### ✔️ static
클래스에 딱 1개만 존재하는 필드/메서드로, 객체를 생성하지 않아도 클래스 이름으로 접근할 수 있어!
static은 클래스에 소속! (인스턴스 아님!) 

static은 클래스에 고정된 "공용 자원"이야.
객체 없이 바로 접근할 수 있고, 모든 인스턴스가 공유해서 쓰는 거다!

#### <static 변수인 count는 모든 인스턴스가 공유함>
```
class Counter {
    static int count = 0;

    Counter() {
        count++;
        System.out.println("count = " + count);
    }
}
```
```
public class Main {
    public static void main(String[] args) {
        new Counter(); // count = 1
        new Counter(); // count = 2
        new Counter(); // count = 3
    }
}
```

#### <static 메서드>
```
class MathUtil {
    static int square(int x) {
        return x * x;
    }
}
```
```
int result = MathUtil.square(5);  // ✅ 객체 생성 없이 바로 호출
```

- 단, static 메서드 안에서는 인스턴스 변수 사용 불가!
- static 메서드에서는 this, super 사용 불가능!

```
static void method() {
    System.out.println(this.value); // ❌ 오류!
}
```
