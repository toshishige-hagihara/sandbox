	.file	"false_sharing2.cpp"
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:
	.string	"***** parallel *****\n"
.LC1:
	.string	"[same cache line] %f sec\n"
.LC3:
	.string	"[same cache line: f] %f sec\n"
.LC4:
	.string	"[same cache line: g] %f sec\n"
	.section	.rodata.str1.8,"aMS",@progbits,1
	.align 8
.LC5:
	.string	"[different cache line] %f sec\n"
	.align 8
.LC6:
	.string	"[different cache line: f] %f sec\n"
	.align 8
.LC7:
	.string	"[different cache line: g] %f sec\n"
	.section	.rodata.str1.1
.LC8:
	.string	"***** serial *****\n"
	.text
.globl main
	.type	main, @function
main:
.LFB43:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	pushq	%r12
	.cfi_def_cfa_offset 16
	pushq	%rbp
	.cfi_def_cfa_offset 24
	pushq	%rbx
	.cfi_def_cfa_offset 32
	subq	$16, %rsp
	.cfi_def_cfa_offset 48
	movl	$.LC0, %esi
	movl	$1, %edi
	movl	$0, %eax
	.cfi_offset 3, -32
	.cfi_offset 6, -24
	.cfi_offset 12, -16
	call	__printf_chk
	call	clock
	movq	%rax, %r12
	leaq	8(%rsp), %rbx
	movl	$counters, %ecx
	movl	$_Z1fPv, %edx
	movl	$0, %esi
	movq	%rbx, %rdi
	call	pthread_create
	movl	$counters+4, %ecx
	movl	$_Z1gPv, %edx
	movl	$0, %esi
	movq	%rsp, %rdi
	call	pthread_create
	movl	$0, %esi
	movq	8(%rsp), %rdi
	call	pthread_join
	movl	$0, %esi
	movq	(%rsp), %rdi
	call	pthread_join
	call	clock
	subq	%r12, %rax
	cvtsi2sdq	%rax, %xmm0
	divsd	.LC2(%rip), %xmm0
	movl	$.LC1, %esi
	movl	$1, %edi
	movl	$1, %eax
	call	__printf_chk
	movq	f_end(%rip), %rax
	subq	f_start(%rip), %rax
	cvtsi2sdq	%rax, %xmm0
	divsd	.LC2(%rip), %xmm0
	movl	$.LC3, %esi
	movl	$1, %edi
	movl	$1, %eax
	call	__printf_chk
	movq	g_end(%rip), %rax
	subq	g_start(%rip), %rax
	cvtsi2sdq	%rax, %xmm0
	divsd	.LC2(%rip), %xmm0
	movl	$.LC4, %esi
	movl	$1, %edi
	movl	$1, %eax
	call	__printf_chk
	call	clock
	movq	%rax, %r12
	movl	$counters2, %ecx
	movl	$_Z1fPv, %edx
	movl	$0, %esi
	movq	%rbx, %rdi
	call	pthread_create
	movl	$counters2+64, %ecx
	movl	$_Z1gPv, %edx
	movl	$0, %esi
	movq	%rsp, %rdi
	call	pthread_create
	movl	$0, %esi
	movq	8(%rsp), %rdi
	call	pthread_join
	movl	$0, %esi
	movq	(%rsp), %rdi
	call	pthread_join
	call	clock
	subq	%r12, %rax
	cvtsi2sdq	%rax, %xmm0
	divsd	.LC2(%rip), %xmm0
	movl	$.LC5, %esi
	movl	$1, %edi
	movl	$1, %eax
	call	__printf_chk
	movq	f_end(%rip), %rax
	subq	f_start(%rip), %rax
	cvtsi2sdq	%rax, %xmm0
	divsd	.LC2(%rip), %xmm0
	movl	$.LC6, %esi
	movl	$1, %edi
	movl	$1, %eax
	call	__printf_chk
	movq	g_end(%rip), %rax
	subq	g_start(%rip), %rax
	cvtsi2sdq	%rax, %xmm0
	divsd	.LC2(%rip), %xmm0
	movl	$.LC7, %esi
	movl	$1, %edi
	movl	$1, %eax
	call	__printf_chk
	movl	$.LC8, %esi
	movl	$1, %edi
	movl	$0, %eax
	call	__printf_chk
	call	clock
	movq	%rax, %r12
	movl	$counters, %ecx
	movl	$_Z1fPv, %edx
	movl	$0, %esi
	movq	%rbx, %rdi
	call	pthread_create
	movl	$0, %esi
	movq	8(%rsp), %rdi
	call	pthread_join
	movl	$counters+4, %ecx
	movl	$_Z1gPv, %edx
	movl	$0, %esi
	movq	%rsp, %rdi
	call	pthread_create
	movl	$0, %esi
	movq	(%rsp), %rdi
	call	pthread_join
	call	clock
	subq	%r12, %rax
	cvtsi2sdq	%rax, %xmm0
	divsd	.LC2(%rip), %xmm0
	movl	$.LC1, %esi
	movl	$1, %edi
	movl	$1, %eax
	call	__printf_chk
	movq	f_end(%rip), %rax
	subq	f_start(%rip), %rax
	cvtsi2sdq	%rax, %xmm0
	divsd	.LC2(%rip), %xmm0
	movl	$.LC3, %esi
	movl	$1, %edi
	movl	$1, %eax
	call	__printf_chk
	movq	g_end(%rip), %rax
	subq	g_start(%rip), %rax
	cvtsi2sdq	%rax, %xmm0
	divsd	.LC2(%rip), %xmm0
	movl	$.LC4, %esi
	movl	$1, %edi
	movl	$1, %eax
	call	__printf_chk
	call	clock
	movq	%rax, %r12
	movl	$counters2, %ecx
	movl	$_Z1fPv, %edx
	movl	$0, %esi
	movq	%rbx, %rdi
	call	pthread_create
	movl	$0, %esi
	movq	8(%rsp), %rdi
	call	pthread_join
	movl	$counters2+64, %ecx
	movl	$_Z1gPv, %edx
	movl	$0, %esi
	movq	%rsp, %rdi
	call	pthread_create
	movl	$0, %esi
	movq	(%rsp), %rdi
	call	pthread_join
	call	clock
	subq	%r12, %rax
	cvtsi2sdq	%rax, %xmm0
	divsd	.LC2(%rip), %xmm0
	movl	$.LC5, %esi
	movl	$1, %edi
	movl	$1, %eax
	call	__printf_chk
	movq	f_end(%rip), %rax
	subq	f_start(%rip), %rax
	cvtsi2sdq	%rax, %xmm0
	divsd	.LC2(%rip), %xmm0
	movl	$.LC6, %esi
	movl	$1, %edi
	movl	$1, %eax
	call	__printf_chk
	movq	g_end(%rip), %rax
	subq	g_start(%rip), %rax
	cvtsi2sdq	%rax, %xmm0
	divsd	.LC2(%rip), %xmm0
	movl	$.LC7, %esi
	movl	$1, %edi
	movl	$1, %eax
	call	__printf_chk
	movl	$0, %eax
	addq	$16, %rsp
	popq	%rbx
	popq	%rbp
	popq	%r12
	ret
	.cfi_endproc
.LFE43:
	.size	main, .-main
.globl _Z1gPv
	.type	_Z1gPv, @function
_Z1gPv:
.LFB42:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	pushq	%rbx
	.cfi_def_cfa_offset 16
	movq	%rdi, %rbx
	.cfi_offset 3, -16
	call	clock
	movq	%rax, g_start(%rip)
	cmpl	$0, counts2(%rip)
	jle	.L4
	movl	$0, %eax
.L5:
	lock addl	$1, (%rbx)
	addl	$1, %eax
	cmpl	%eax, counts2(%rip)
	jg	.L5
.L4:
	call	clock
	movq	%rax, g_end(%rip)
	movl	$0, %eax
	popq	%rbx
	ret
	.cfi_endproc
.LFE42:
	.size	_Z1gPv, .-_Z1gPv
.globl _Z1fPv
	.type	_Z1fPv, @function
_Z1fPv:
.LFB41:
	.cfi_startproc
	.cfi_personality 0x3,__gxx_personality_v0
	pushq	%rbx
	.cfi_def_cfa_offset 16
	movq	%rdi, %rbx
	.cfi_offset 3, -16
	call	clock
	movq	%rax, f_start(%rip)
	cmpl	$0, counts(%rip)
	jle	.L9
	movl	$0, %eax
.L10:
	lock addl	$1, (%rbx)
	addl	$1, %eax
	cmpl	%eax, counts(%rip)
	jg	.L10
.L9:
	call	clock
	movq	%rax, f_end(%rip)
	movl	$0, %eax
	popq	%rbx
	ret
	.cfi_endproc
.LFE41:
	.size	_Z1fPv, .-_Z1fPv
.globl counts
	.data
	.align 4
	.type	counts, @object
	.size	counts, 4
counts:
	.long	20000000
.globl counts2
	.align 4
	.type	counts2, @object
	.size	counts2, 4
counts2:
	.long	10000000
.globl counters
	.bss
	.align 4
	.type	counters, @object
	.size	counters, 8
counters:
	.zero	8
.globl counters2
	.align 32
	.type	counters2, @object
	.size	counters2, 128
counters2:
	.zero	128
.globl f_start
	.align 8
	.type	f_start, @object
	.size	f_start, 8
f_start:
	.zero	8
.globl f_end
	.align 8
	.type	f_end, @object
	.size	f_end, 8
f_end:
	.zero	8
.globl g_start
	.align 8
	.type	g_start, @object
	.size	g_start, 8
g_start:
	.zero	8
.globl g_end
	.align 8
	.type	g_end, @object
	.size	g_end, 8
g_end:
	.zero	8
	.section	.rodata.cst8,"aM",@progbits,8
	.align 8
.LC2:
	.long	0
	.long	1093567616
	.ident	"GCC: (Ubuntu/Linaro 4.4.4-14ubuntu5) 4.4.5"
	.section	.note.GNU-stack,"",@progbits
