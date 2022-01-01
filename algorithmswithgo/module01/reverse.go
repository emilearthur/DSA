package module01

import "strings"

// Reverse will return the provided word in reverse
// order. Eg:
//
//   Reverse("cat") => "tac"
//   Reverse("alphabet") => "tebahpla"
//
func Reverse(word string) string {
	if len(word) == 0 {
		return ""
	}
	var rev string
	for _, v := range word {
		rev = string(v) + rev
	}
	return string(rev)
}

// Reverse1 - other method
func Reverse1(word string) string {
	if len(word) == 0 {
		return ""
	}
	var rev []byte
	for i := len(word) - 1; i >= 0; i-- {
		rev = append(rev, word[i])
	}
	return string(rev)
}

// Reverse2 - other method
func Reverse2(word string) string {
	if len(word) == 0 {
		return ""
	}
	var res string
	for i := 0; i < len(word); i++ {
		res = string(word[i]) + res
	}
	return res
}

// ReverseUsingBuilder uses stringbuilder for construct
func ReverseUsingBuilder(word string) string {
	if len(word) == 0 {
		return ""
	}
	var sb strings.Builder
	for i := len(word) - 1; i >= 0; i-- {
		sb.WriteByte(word[i])
	}
	return sb.String()
}
