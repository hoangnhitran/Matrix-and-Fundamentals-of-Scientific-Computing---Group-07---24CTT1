from manim import *

class CholeskyDecompositionScene(Scene):
    def construct(self):
        # ==========================================
        # PHẦN 1: GIỚI THIỆU BÀI TOÁN
        # ==========================================
        title = Text("Đồ Án 1: Phân Rã Cholesky & Chéo Hóa", font_size=36, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # ==========================================
        # PHẦN 1: NHẮC LẠI LÝ THUYẾT
        # ==========================================
        # 1. Lý Thuyết: Chéo Hóa Ma Trận (Frame 1)
        theory1_title = Text("1. Lý Thuyết: Chéo Hóa Ma Trận", font_size=28, color=YELLOW)
        theory1_title.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(theory1_title))
        
        theory1_eq = MathTex("A = P D P^{-1}").scale(1.2)
        theory1_eq2 = MathTex(r"D = \text{diag}(\lambda_1, \lambda_2, \dots, \lambda_n)").scale(1.2)
        theory1_group = VGroup(theory1_eq, theory1_eq2).arrange(DOWN, buff=0.5)
        theory1_group.next_to(theory1_title, DOWN, buff=1.0)
        
        self.play(Write(theory1_eq))
        self.play(Write(theory1_eq2))
        self.wait(2)
        
        theory1_desc1 = Text("P là ma trận chứa các vector riêng", font_size=24)
        theory1_desc2_math = MathTex(r"\lambda_i").scale(0.9)
        theory1_desc2_text = Text(" là các giá trị riêng (eigenvalues) của A", font_size=24)
        theory1_desc2 = VGroup(theory1_desc2_math, theory1_desc2_text).arrange(RIGHT, buff=0.15)
        
        theory1_desc_group = VGroup(theory1_desc1, theory1_desc2).arrange(DOWN, buff=0.3)
        theory1_desc_group.next_to(theory1_group, DOWN, buff=0.8)
        self.play(FadeIn(theory1_desc_group))
        self.wait(4)
        
        self.play(FadeOut(theory1_group), FadeOut(theory1_desc_group))
        
        # 1. Lý Thuyết: Chéo Hóa Ma Trận (Frame 2 - Ứng dụng)
        theory1_app_title = Text("Ứng dụng của Chéo hóa:", font_size=26, color=GREEN)
        theory1_app_title.next_to(theory1_title, DOWN, buff=1.0)
        self.play(FadeIn(theory1_app_title))
        
        theory1_app_eq = MathTex("A^k = P D^k P^{-1}").scale(1.5)
        theory1_app_eq.next_to(theory1_app_title, DOWN, buff=0.8)
        self.play(Write(theory1_app_eq))
        self.wait(2)
        
        theory1_comp1_text = Text("Giảm chi phí tính", font_size=24)
        theory1_comp1_math = MathTex("A^k").scale(0.9)
        theory1_comp1_text2 = Text("từ", font_size=24)
        theory1_comp1_math2 = MathTex(r"\mathcal{O}(n^3 \log k)").scale(0.9)
        comp_line1 = VGroup(theory1_comp1_text, theory1_comp1_math, theory1_comp1_text2, theory1_comp1_math2).arrange(RIGHT, buff=0.15)
        
        theory1_comp2_text = Text("xuống chỉ còn", font_size=24)
        theory1_comp2_math = MathTex(r"\mathcal{O}(n^2)").scale(0.9)
        comp_line2 = VGroup(theory1_comp2_text, theory1_comp2_math).arrange(RIGHT, buff=0.15)
        
        theory1_complexity = VGroup(comp_line1, comp_line2).arrange(DOWN, buff=0.2)
        theory1_complexity.next_to(theory1_app_eq, DOWN, buff=0.8)
        self.play(FadeIn(theory1_complexity))
        self.wait(5)
        
        self.play(FadeOut(theory1_title), FadeOut(theory1_app_title), FadeOut(theory1_app_eq), FadeOut(theory1_complexity))
        
        # 2. Lý Thuyết: Phân Rã Cholesky
        theory2_title = Text("2. Lý Thuyết: Phân Rã Cholesky", font_size=28, color=YELLOW)
        theory2_title.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(theory2_title))
        
        # 2. Lý Thuyết: Phân Rã Cholesky (Frame 1 - Định nghĩa)
        theory2_cond = Text("Điều kiện: Ma trận A đối xứng xác định dương (SPD)", font_size=24)
        theory2_cond.next_to(theory2_title, DOWN, buff=1.0)
        self.play(Write(theory2_cond))
        
        theory2_eq = MathTex("A = LL^T").scale(1.5)
        theory2_desc = Text("L là ma trận tam giác dưới", font_size=24)
        theory2_def_group = VGroup(theory2_eq, theory2_desc).arrange(DOWN, buff=0.3)
        theory2_def_group.next_to(theory2_cond, DOWN, buff=0.8)
        self.play(Write(theory2_def_group))
        self.wait(3)
        
        self.play(FadeOut(theory2_cond), FadeOut(theory2_def_group))
        
        # 2. Lý Thuyết: Phân Rã Cholesky (Frame 2 - Công thức)
        theory2_form_title = Text("Công thức truy hồi:", font_size=26, color=GREEN)
        theory2_form_title.next_to(theory2_title, DOWN, buff=0.8)
        self.play(FadeIn(theory2_form_title))
        
        theory2_f1 = MathTex(r"L_{jj} = \sqrt{ A_{jj} - \sum_{k=1}^{j-1} L_{jk}^2 }").scale(0.9)
        theory2_f2 = MathTex(r"L_{ij} = \frac{1}{L_{jj}} \left( A_{ij} - \sum_{k=1}^{j-1} L_{ik} L_{jk} \right), \quad i > j").scale(0.9)
        theory2_formulas = VGroup(theory2_f1, theory2_f2).arrange(DOWN, buff=0.8)
        theory2_formulas.next_to(theory2_form_title, DOWN, buff=0.8)
        self.play(FadeIn(theory2_formulas))
        self.wait(5)
        
        self.play(FadeOut(theory2_form_title), FadeOut(theory2_formulas))
        
        # 2. Lý Thuyết: Phân Rã Cholesky (Frame 3 - Hiệu năng)
        theory2_perf_title = Text("Hiệu năng tính toán:", font_size=26, color=GREEN)
        theory2_perf_title.next_to(theory2_title, DOWN, buff=1.0)
        self.play(FadeIn(theory2_perf_title))
        
        theory2_comp1_text = Text("Chi phí tính toán =", font_size=24)
        theory2_comp1_math = MathTex(r"\frac{1}{2}").scale(1.2)
        theory2_comp1_text2 = Text("Phân rã LU", font_size=24)
        theory2_comp = VGroup(theory2_comp1_text, theory2_comp1_math, theory2_comp1_text2).arrange(RIGHT, buff=0.2)
        theory2_comp.next_to(theory2_perf_title, DOWN, buff=0.8)
        self.play(Write(theory2_comp))
        self.wait(2)
        
        theory2_adv = Text("→ Lợi thế cực lớn về mặt hiệu năng với ma trận SPD!", font_size=26, color=YELLOW)
        theory2_adv.next_to(theory2_comp, DOWN, buff=0.8)
        self.play(FadeIn(theory2_adv))
        self.wait(5)
        
        self.play(FadeOut(theory2_title), FadeOut(theory2_perf_title), FadeOut(theory2_comp), FadeOut(theory2_adv))
        
        # ==========================================
        # PHẦN 2: VÍ DỤ THUẬT TOÁN
        # ==========================================
        demo_title = Text("3. Ví dụ thuật toán", font_size=28, color=YELLOW)
        demo_title.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(demo_title))
        self.wait(2)
        self.play(FadeOut(demo_title))

        intro_text = Text("3.1. Giới thiệu ma trận A", font_size=28, color=YELLOW)
        intro_text.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(intro_text))

        A_matrix = Matrix([
            [4, 12, -16],
            [12, 37, -43],
            [-16, -43, 98]
        ])
        A_label = MathTex("A = ")
        A_group = VGroup(A_label, A_matrix).arrange(RIGHT)
        self.play(FadeIn(A_group))
        self.wait(4)

        goal_text_p1 = Text("Mục tiêu: Tìm L sao cho ", font_size=24)
        goal_math_p1 = MathTex("A = LL^T")
        goal_text_p2 = Text(" và ", font_size=24)
        goal_math_p2 = MathTex("A = PDP^{-1}")

        goal_text = VGroup(goal_text_p1, goal_math_p1, goal_text_p2, goal_math_p2).arrange(RIGHT, buff=0.2)
        goal_text.next_to(A_group, DOWN, buff=1.0)
        self.play(Write(goal_text))
        self.wait(5)

        self.play(FadeOut(intro_text), FadeOut(goal_text))
        self.play(A_group.animate.scale(0.65).to_corner(UL).shift(DOWN * 1.5))

        # ==========================================
        # PHẦN 2: TRỰC QUAN HÓA QUÁ TRÌNH PHÂN RÃ
        # ==========================================
        # 3.2 Hiển thị tính chất SPD
        step1_text = Text("3.2. Kiểm tra tính chất SPD (Đối xứng Xác định Dương)", font_size=28, color=YELLOW)
        step1_text.to_edge(UP).shift(DOWN * 0.8)
        self.play(FadeIn(step1_text))

        spd_desc = Text("Các định thức con chính\n(Leading Principal Minors) > 0:", font_size=24)
        spd_desc.next_to(A_group, RIGHT, buff=1.0).align_to(A_group, UP)
        self.play(Write(spd_desc))

        # Show determinants
        det1 = MathTex(r"\Delta_1 = 4 > 0")
        det2 = MathTex(r"\Delta_2 = \det \begin{bmatrix} 4 & 12 \\ 12 & 37 \end{bmatrix} = 4(37) - 12(12) = 4 > 0")
        det3 = MathTex(r"\Delta_3 = \det(A) = 36 > 0")
        dets = VGroup(det1, det2, det3).arrange(DOWN, aligned_edge=LEFT).scale(0.8)
        dets.next_to(spd_desc, DOWN, buff=0.5).align_to(spd_desc, LEFT)
        
        self.play(FadeIn(det1))
        self.wait(3)
        self.play(FadeIn(det2))
        self.wait(3)
        self.play(FadeIn(det3))
        self.wait(3)

        spd_conclusion = Text("=> A đủ điều kiện phân rã Cholesky", font_size=26, color=GREEN)
        spd_conclusion.next_to(dets, DOWN, buff=0.5).align_to(dets, LEFT)
        self.play(Write(spd_conclusion))
        self.wait(3)

        self.play(FadeOut(step1_text), FadeOut(spd_desc), FadeOut(dets), FadeOut(spd_conclusion))

        # 3.3 Từng bước tính L
        step2_text = Text("3.3. Từng bước tính ma trận tam giác dưới L", font_size=28, color=YELLOW)
        step2_text.to_edge(UP).shift(DOWN * 0.8)
        self.play(FadeIn(step2_text))

        L_matrix = Matrix([
            ["L_{11}", "0", "0"],
            ["L_{21}", "L_{22}", "0"],
            ["L_{31}", "L_{32}", "L_{33}"]
        ])
        L_label = MathTex("L = ")
        L_group = VGroup(L_label, L_matrix).arrange(RIGHT).scale(0.65)
        L_group.next_to(A_group, DOWN, buff=0.5).align_to(A_group, LEFT)
        
        self.play(FadeIn(L_group))
        self.wait(1)

        # Công thức hiện tại đang tính
        calc_formula = MathTex("").scale(0.75)
        calc_formula.next_to(L_group, RIGHT, buff=0.8)

        # Các bước tính toán và thay thế
        steps = [
            (0, r"L_{11} = \sqrt{A_{11}} = \sqrt{4} = 2", "2"),
            (3, r"L_{21} = \frac{A_{21}}{L_{11}} = \frac{12}{2} = 6", "6"),
            (6, r"L_{31} = \frac{A_{31}}{L_{11}} = \frac{-16}{2} = -8", "-8"),
            (4, r"L_{22} = \sqrt{A_{22} - L_{21}^2} = \sqrt{37 - 36} = 1", "1"),
            (7, r"L_{32} = \frac{A_{32} - L_{31}L_{21}}{L_{22}} = \frac{-43 - (-8)(6)}{1} = 5", "5"),
            (8, r"L_{33} = \sqrt{A_{33} - L_{31}^2 - L_{32}^2} = \sqrt{98 - 64 - 25} = 3", "3")
        ]

        entries = L_matrix.get_entries()

        for index, tex_string, result_str in steps:
            # Hiển thị công thức
            new_formula = MathTex(tex_string).scale(0.75).next_to(L_group, RIGHT, buff=0.8)
            self.play(Transform(calc_formula, new_formula))
            self.wait(3.5) # Dừng lâu để đọc công thức
            
            # Cập nhật số vào ma trận L
            result_mob = MathTex(result_str).scale(0.65).move_to(entries[index])
            self.play(
                entries[index].animate.set_opacity(0),
                FadeIn(result_mob)
            )
            self.wait(2)

        final_L_text = Text("Hoàn thành phân rã A = LLᵀ", font_size=28, color=GREEN)
        final_L_text.next_to(calc_formula, DOWN, buff=1)
        self.play(Write(final_L_text))
        self.wait(4)

        # Dọn dẹp để sang phần 3
        mobs_to_fade = [m for m in self.mobjects if m != title]
        self.play(FadeOut(Group(*mobs_to_fade)))
        self.wait(2)

        # ==========================================
        # PHẦN 3: CHÉO HÓA (DIAGONALIZATION)
        # ==========================================
        step3_text = Text("3.4. Chéo Hóa Ma Trận A = P D P⁻¹", font_size=28, color=YELLOW)
        step3_text.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(step3_text))

        # Hiển thị giá trị riêng
        eigval_title = Text("Giá trị riêng (Eigenvalues):", font_size=24)
        eigvals = MathTex(r"\lambda_1 \approx 0.0188, \quad \lambda_2 \approx 15.504, \quad \lambda_3 \approx 123.4772")
        eigval_group = VGroup(eigval_title, eigvals).arrange(DOWN)
        eigval_group.shift(UP * 1.5)
        self.play(Write(eigval_group))
        self.wait(4)

        # Hiển thị D và P
        D_matrix = Matrix([
            ["0.0188", "0", "0"],
            ["0", "15.504", "0"],
            ["0", "0", "123.4772"]
        ], h_buff=2.5).scale(0.7)
        D_label = MathTex("D = ")
        D_group = VGroup(D_label, D_matrix).arrange(RIGHT)

        P_matrix = Matrix([
            ["0.9634", "0.2127", "-0.163"],
            ["-0.2648", "0.849", "-0.4573"],
            ["0.0411", "0.4838", "0.8742"]
        ], h_buff=2.0).scale(0.7)
        P_label = MathTex("P = ")
        P_group = VGroup(P_label, P_matrix).arrange(RIGHT)

        matrices_group = VGroup(D_group, P_group).arrange(RIGHT, buff=1.5)
        matrices_group.next_to(eigval_group, DOWN, buff=1)
        
        self.play(FadeIn(D_group))
        self.wait(2)
        
        p_desc = Text("P  chứa  các  vector  riêng  tương  ứng  ở  dạng  cột", font_size=28, color=LIGHT_GREY).scale(0.7)
        p_desc.next_to(P_group, DOWN, buff=0.3)
        self.play(FadeIn(P_group), Write(p_desc))
        self.wait(4)

        # Dọn dẹp không gian
        self.play(FadeOut(eigval_group), FadeOut(p_desc))
        self.play(matrices_group.animate.next_to(step3_text, DOWN, buff=0.5))

        # Kết luận: Hiện công thức và text xanh trước
        final_eq = MathTex("A", "=", "P", "D", "P^{-1}").scale(1.5)
        final_eq.next_to(matrices_group, DOWN, buff=0.8)
        
        self.play(
            Write(final_eq[0:2]),
            TransformFromCopy(P_group, final_eq[2]),
            TransformFromCopy(D_group, final_eq[3]),
            TransformFromCopy(P_group, final_eq[4])
        )
        self.wait(3)
        
        conclude_text = Text("Với ma trận đối xứng, P là ma trận trực giao (P⁻¹ = Pᵀ)", font_size=24, color=GREEN)
        conclude_text.next_to(final_eq, DOWN, buff=0.5)
        self.play(Write(conclude_text))
        self.wait(4)

        # Xóa final_eq và text xanh để lấy không gian hiển thị ma trận P^-1
        self.play(FadeOut(final_eq), FadeOut(conclude_text))

        # Hiển thị P^-1
        P_inv_matrix = Matrix([
            ["0.9634", "-0.2648", "0.0411"],
            ["0.2127", "0.849", "0.4838"],
            ["-0.163", "-0.4573", "0.8742"]
        ], h_buff=1.8).scale(0.7)
        P_inv_label = MathTex("P^{-1} = P^T = ")
        P_inv_group = VGroup(P_inv_label, P_inv_matrix).arrange(RIGHT)
        P_inv_group.scale(0.9)  # Thu nhỏ nhẹ để vừa chiều ngang
        P_inv_group.next_to(matrices_group, DOWN, buff=0.8)
        
        self.play(FadeIn(P_inv_group))
        self.wait(5)

        final_text = Text("Hoàn thành quá trình chéo hóa!", font_size=32, color=YELLOW)
        final_text.next_to(P_inv_group, DOWN, buff=0.5)
        self.play(Write(final_text))
        
        self.wait(8)